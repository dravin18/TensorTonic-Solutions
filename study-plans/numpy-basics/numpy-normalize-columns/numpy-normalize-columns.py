import numpy as np

def normalize(data):
    """Returns: np.ndarray of shape (m, n), z-score normalized per column"""
    data = np.asarray(data, dtype = np.float64)
    mean = data.mean(axis = 0)
    std = data.std(axis = 0)
    z_score = (data - mean) / std
    return z_score