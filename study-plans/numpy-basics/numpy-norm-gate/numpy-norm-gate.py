import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""
    X = np.asarray(X, dtype = np.float64)
    W = np.asarray(W, dtype = np.float64)
    Y = X @ W
    norm = np.linalg.norm(Y, axis = 1)
    output = np.where(norm[:, np.newaxis]>= threshold, Y, 0.0)
    return output