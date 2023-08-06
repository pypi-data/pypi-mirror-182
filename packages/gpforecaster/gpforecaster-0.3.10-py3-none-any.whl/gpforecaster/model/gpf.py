import torch
import numpy as np
import gpytorch
from .gp import ExactGPModel
from .mean_functions import PiecewiseLinearMean
from gpytorch.mlls import SumMarginalLogLikelihood
from gpforecaster.results.calculate_metrics import CalculateResultsBottomUp
import pickle
from pathlib import Path
from sklearn.preprocessing import StandardScaler
import time
import matplotlib.pyplot as plt
import psutil
import os
from gpforecaster.utils.logger import Logger
from datetime import timedelta


class GPF:
    def __init__(
        self,
        dataset,
        groups,
        input_dir="./",
        n_samples=500,
        store_prediction_samples=False,
        store_prediction_points=False,
        log_dir="."
    ):
        self.dataset = dataset
        self.groups = groups
        self.input_dir = input_dir
        self.timer_start = time.time()
        self.wall_time_train = None
        self.wall_time_predict = None
        self.wall_time_total = None
        self.groups, self.scaler = self._preprocess(self.groups)
        self._create_directories()
        self.n_samples = n_samples
        self.store_prediction_samples = store_prediction_samples
        self.store_prediction_points = store_prediction_points

        self.train_x = torch.arange(groups["train"]["n"])
        self.train_x = self.train_x.type(torch.DoubleTensor)
        self.train_x = self.train_x.unsqueeze(-1)
        self.train_y = torch.from_numpy(groups["train"]["data"])

        self.test_x = torch.arange(groups["train"]["n"], groups["predict"]["n"])
        self.test_x = self.test_x.type(torch.DoubleTensor)
        self.test_x = self.test_x.unsqueeze(-1)
        self.test_y = torch.from_numpy(
            groups["predict"]["data_matrix"][groups["train"]["n"] :]
        )

        self.losses = []
        self.val_losses = []

        self.logger_train = Logger("train", to_file=True, log_dir=log_dir)
        self.logger_metrics = Logger("metrics", to_file=True, log_dir=log_dir)

    def _create_directories(self):
        # Create directory to store results if does not exist
        Path(f"{self.input_dir}results").mkdir(parents=True, exist_ok=True)

    def _preprocess(self, groups):
        scaler = StandardScaler()
        scaler.fit(self.groups["train"]["data"])
        groups["train"]["data"] = scaler.transform(groups["train"]["data"])
        groups["predict"]["data_matrix"] = scaler.transform(
            groups["predict"]["data_matrix"]
        )

        return groups, scaler

    def _build_mixtures(self):
        # build the matrix

        #     Group1     |   Group2
        # GP1, GP2, GP3  | GP1, GP2
        # 0  , 1  , 1    | 0  , 1
        # 1  , 0  , 0    | 1  , 0
        # 0  , 1, , 1    | 0  , 1
        # 1  , 0  , 1    | 1  , 0

        idxs = []
        for k, val in self.groups["train"]["groups_idx"].items():
            idxs.append(val)

        idxs_t = np.array(idxs).T

        n_groups = np.sum(
            np.fromiter(self.groups["train"]["groups_n"].values(), dtype="int32")
        )
        known_mixtures = np.zeros((self.groups["train"]["s"], n_groups))
        k = 0
        for j in range(self.groups["train"]["g_number"]):
            for i in range(np.max(idxs_t[:, j]) + 1):
                idx_to_1 = np.where(idxs_t[:, j] == i)
                known_mixtures[:, k][idx_to_1] = 1
                k += 1

        top_level = np.ones((known_mixtures.shape[0], 1))
        known_mixtures = np.concatenate((known_mixtures, top_level), axis=1)
        n_groups += 1

        return known_mixtures, n_groups

    def _build_cov_matrices(self):
        known_mixtures, n_groups = self._build_mixtures()
        covs = []
        for i in range(1, n_groups + 1):
            # RBF kernel
            rbf_kernel = gpytorch.kernels.RBFKernel()
            rbf_kernel.lengthscale = torch.tensor([1.0])
            scale_rbf_kernel = gpytorch.kernels.ScaleKernel(rbf_kernel)
            scale_rbf_kernel.outputscale = torch.tensor([0.5])

            # Periodic Kernel
            periodic_kernel = gpytorch.kernels.PeriodicKernel()
            periodic_kernel.period_length = torch.tensor([self.groups["seasonality"]])
            periodic_kernel.lengthscale = torch.tensor([0.5])
            scale_periodic_kernel = gpytorch.kernels.ScaleKernel(periodic_kernel)
            scale_periodic_kernel.outputscale = torch.tensor([1.5])

            # Cov Matrix
            cov = scale_rbf_kernel + scale_periodic_kernel
            covs.append(cov)

        return covs, known_mixtures, n_groups

    def _apply_mixture_cov_matrices(self):
        covs, known_mixtures, n_groups = self._build_cov_matrices()

        # apply mixtures to covariances
        selected_covs = []
        mixed_covs = []
        for i in range(self.groups["train"]["s"]):
            mixture_weights = known_mixtures[i]
            for w_ix in range(n_groups):
                w = mixture_weights[w_ix]
                if w == 1.0:
                    selected_covs.append(covs[w_ix])
            mixed_cov = selected_covs[0]
            for cov in range(1, len(selected_covs)):
                mixed_cov += selected_covs[
                    cov
                ]  # because GP(cov1 + cov2) = GP(cov1) + GP(cov2)
            mixed_covs.append(mixed_cov)
            selected_covs = []  # clear out cov list

        return mixed_covs

    def _build_model(self, x, y):
        mixed_covs = self._apply_mixture_cov_matrices()
        n_changepoints = 4
        changepoints = np.linspace(0, self.groups["train"]["n"], n_changepoints + 2)[
            1:-1
        ]

        model_list = []
        likelihood_list = []
        for i in range(self.groups["train"]["s"]):
            likelihood_list.append(gpytorch.likelihoods.GaussianLikelihood())
            model_list.append(
                ExactGPModel(
                    x,
                    y[:, i],
                    likelihood_list[i],
                    mixed_covs[i],
                    changepoints,
                    PiecewiseLinearMean,
                )
            )

        return likelihood_list, model_list

    def early_stopping(self, patience):
        losses = [x for x in self.val_losses if x is not None]
        losses.reverse()
        non_decreasing = 0
        for x, y in zip(losses, losses[1:]):
            if x >= y:
                non_decreasing += 1
            else:
                break

        if non_decreasing > patience:
            return True
        else:
            return False

    def train(
        self,
        n_iterations=500,
        lr=1e-3,
        early_stopping=True,
        patience=100,
        verbose=True,
        track_mem=False
    ):
        likelihood_list, model_list = self._build_model(x=self.train_x, y=self.train_y)

        model = gpytorch.models.IndependentModelList(*model_list)
        likelihood = gpytorch.likelihoods.LikelihoodList(*likelihood_list)

        mll = SumMarginalLogLikelihood(likelihood, model)

        model.train()
        likelihood.train()

        optimizer = torch.optim.Adam(
            model.parameters(), lr=lr
        )  # Includes GaussianLikelihood parameters

        for i in range(n_iterations):
            optimizer.zero_grad()
            output = model(*model.train_inputs)
            loss = -mll(output, model.train_targets)
            self.losses.append(loss.item())

            if early_stopping:
                if i % 5 == 0:
                    model.eval()
                    likelihood.eval()
                    val_loss = self.validate(model, mll)
                    if self.early_stopping(patience=patience):
                        break
                    if verbose:
                        print(
                            f"Iter {i}/{n_iterations} - Loss: {np.round(loss.item(), 3)}, Validation Loss: {np.round(val_loss, 3)}"
                        )
                    # switch to train mode
                    model.train()
                    likelihood.train()
                else:
                    self.val_losses.append(None)
            else:
                if verbose:
                    print(f"Iter {i}/{n_iterations} - Loss: {np.round(loss.item(), 3)}")

            loss.backward()
            optimizer.step()

            if i % 30 == 0 and track_mem:
                # Track RAM usage
                process = psutil.Process(os.getpid())
                mem = process.memory_info().rss / (1024**3)
                self.logger_train.info(f"train used {mem:.3f} GB of RAM")

        self.wall_time_train = (
            time.time() - self.timer_start
        )
        td = timedelta(seconds=int(time.time() - self.timer_start))
        self.logger_train.info(f"Num epochs {i}")
        self.logger_train.info(f"wall time train {str(td)}")

        self.logger_train.info(f"Val Loss {np.round(loss.item(), 2)}")
        self.logger_train.info(f"Loss {np.round(val_loss, 2)}")

        return model, likelihood

    def validate(self, model, mll):
        with torch.no_grad(), gpytorch.settings.fast_pred_var():
            likelihood_list_val, model_list_val = self._build_model(
                x=self.test_x, y=self.test_y
            )
            model_val = gpytorch.models.IndependentModelList(*model_list_val)
            val_output = model(*model_val.train_inputs)
            val_loss = -mll(val_output, model_val.train_targets)
            self.val_losses.append(float(val_loss.item()))
        return val_loss.item()

    def plot_losses(self):
        n_iterations = np.arange(len(self.losses))
        plt.plot(n_iterations, self.losses)
        plt.plot(n_iterations, self.val_losses, marker="*")
        timestamp = time.strftime("%Y%m%d-%H%M%S", time.gmtime())
        plt.savefig(
            f"./plots/gpf_loss_{self.dataset}_{timestamp}.pdf", format="pdf", bbox_inches="tight"
        )
        plt.show()

    def predict(self, model, likelihood, clip=True):
        timer_start = time.time()

        model.eval()
        likelihood.eval()

        with torch.no_grad(), gpytorch.settings.fast_pred_var():
            test_x = torch.arange(self.groups["predict"]["n"]).type(torch.DoubleTensor)
            predictions = likelihood(
                *model(*[test_x for i in range(self.groups["predict"]["s"])])
            )

        i = 0
        samples = np.zeros(
            (self.n_samples, self.groups["predict"]["n"], self.groups["predict"]["s"])
        )
        for pred in predictions:
            samples[:, :, i] = np.random.normal(
                pred.mean.detach().numpy(),
                np.sqrt(pred.variance.detach().numpy()),
                size=(self.n_samples, self.groups["predict"]["n"]),
            )
            i += 1

        samples = np.transpose(samples, (1, 2, 0))

        # transform back the data
        samples = (
            samples * np.sqrt(self.scaler.var_)[np.newaxis, :, np.newaxis]
        ) + self.scaler.mean_[np.newaxis, :, np.newaxis]
        self.groups["train"]["data"] = self.scaler.inverse_transform(
            self.groups["train"]["data"]
        )
        self.groups["predict"]["data_matrix"] = self.scaler.inverse_transform(
            self.groups["predict"]["data_matrix"]
        )

        # Clip predictions to 0 if there are negative numbers
        if clip:
            samples[samples < 0] = 0

        self.wall_time_predict = time.time() - timer_start
        return samples

    def store_metrics(self, res):
        with open(
            f"{self.input_dir}results/results_gp_cov_{self.dataset}.pickle", "wb"
        ) as handle:
            pickle.dump(res, handle, pickle.HIGHEST_PROTOCOL)

    def metrics(self, samples):
        calc_results = CalculateResultsBottomUp(
            samples,
            self.groups,
            self.store_prediction_samples,
            self.store_prediction_points,
        )
        res = calc_results.calculate_metrics()
        for metric, results in res.items():
            for group, result in results.items():
                if 'ind' not in group:
                    self.logger_metrics.info(f"{metric} for {group}: {np.round(result, 2)}")

        self.wall_time_total = time.time() - self.timer_start

        res["wall_time"] = {}
        res["wall_time"]["wall_time_train"] = self.wall_time_train
        res["wall_time"]["wall_time_predict"] = self.wall_time_predict
        res["wall_time"]["wall_time_total"] = self.wall_time_total

        return res
