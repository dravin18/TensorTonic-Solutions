import numpy as np

def norm_diff(a, b, lo, hi):
    """Returns: np.ndarray of absolute differences after clipping and rescaling to [0, 1]"""
    a = np.asarray(a)
    b = np.asarray(b)
    a_clip = np.clip(a, lo, hi)
    b_clip = np.clip(b, lo, hi)
    a_norm = (a_clip - lo) / (hi - lo)
    b_norm = (b_clip - lo) / (hi - lo)
    
    return np.abs(a_norm - b_norm)