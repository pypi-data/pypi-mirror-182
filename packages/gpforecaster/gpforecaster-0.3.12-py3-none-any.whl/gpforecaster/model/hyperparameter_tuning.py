from typing import Tuple, Dict
import random

from gpforecaster.model.gpf import GPF
from gpforecaster.utils.logger import Logger


def optimize_hyperparameters(
    dataset_name: str, hierarchical_data: Dict, num_trials: int = 20
) -> Tuple[float, float, str, float]:
    """
    Performs a random search to optimize the hyperparameters of the model.

    Parameters
        dataset: Dataset to run hyperparameter tuning
        hierarchical_data: Dict containing data and metadata
        num_trials: Number of trials to perform

    Returns
        best_hyperparameters : A tuple containing the optimal learning rate,
            weight decay, and scheduler type.
    """
    logger_tuning = Logger("hyperparameter_tuning", dataset=dataset_name, to_file=True)
    # Set the hyperparameter search space
    learning_rates = [1e-2, 1e-3]
    weight_decays = [1e-3, 1e-4, 1e-5]
    scheduler_types = ["step", "exponential", "cosine", "none"]

    results = []

    for trial in range(num_trials):
        # Sample hyperparameters randomly
        learning_rate = random.choice(learning_rates)
        weight_decay = random.choice(weight_decays)
        scheduler_type = random.choice(scheduler_types)

        gpf = GPF(dataset=dataset_name, groups=hierarchical_data)

        # Evaluate the performance with the sampled hyperparameters
        model, _ = gpf.train(
            lr=learning_rate,
            weight_decay=weight_decay,
            scheduler_type=scheduler_type,
        )

        val_loss = gpf.validate(model)

        results.append((learning_rate, weight_decay, scheduler_type, val_loss))

    results.sort(key=lambda x: x[3])
    best_hyperparameters = results[0]

    logger_tuning.info(
        f"Best hyperparameters: learning rate = {best_hyperparameters[0]}, weight decay = {best_hyperparameters[1]}, scheduler = {best_hyperparameters[2]}"
    )
    logger_tuning.info(f"Validation loss: {best_hyperparameters[3]}")

    return best_hyperparameters
