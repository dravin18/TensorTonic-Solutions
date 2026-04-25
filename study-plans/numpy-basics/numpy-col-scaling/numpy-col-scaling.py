import numpy as np

def scale_cols(data, weights):
    """Returns: np.ndarray of shape (m, n), each column scaled by corresponding weight"""
    data = np.asarray(data, dtype = np.float64)
    # data = data.T
    weights = np.asarray(weights, dtype = np.float64)
    # weights = weights[:, None]
    ans = data * weights 
    return ans