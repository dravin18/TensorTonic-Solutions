import numpy as np

def priority_replay_sample(priorities: list, alpha: float, beta: float) -> list:
    """
    Returns sampling probabilities and normalized importance weights.
    """
    # Write code here
    priorities = np.asarray(priorities)
    priorities = priorities**alpha
    priorities_sum = sum(priorities)
    sampling_priority = priorities / priorities_sum
    sampling_weights = (len(sampling_priority) * sampling_priority)**(-beta)
    max_weights = max(sampling_weights)
    norm_weights = sampling_weights / max_weights
    return [list(sampling_priority), list(norm_weights)]