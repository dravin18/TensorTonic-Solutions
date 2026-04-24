import numpy as np

def scale_rows(data, weights):
    """Returns: np.ndarray of shape (m, n), each row scaled by corresponding weight"""
    data = np.asarray(data, dtype = np.float64)
    weights = np.asarray(weights, dtype = np.float64)
    weights = weights.reshape(-1,1)
    return data * weights