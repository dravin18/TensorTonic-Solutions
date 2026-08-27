import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x)
    x_mean = np.mean(x)
    var = float(np.sum((x - x_mean)**2)/(x.shape[0] - 1))
    std = float(np.sqrt(var))
    return {'variance' : var, 'standard_deviation' : std}