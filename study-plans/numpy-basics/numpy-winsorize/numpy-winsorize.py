import numpy as np

def winsorize(data, lo_q, hi_q):
    """Returns: np.ndarray of shape (3, m, n), stacked clipped values, lo_mask, hi_mask"""
    data = np.asarray(data, dtype = np.float64)
    lo = np.percentile(data, lo_q, axis=0)
    hi = np.percentile(data, hi_q, axis=0)
    return np.stack([np.clip(data, lo, hi), data < lo, data > hi])