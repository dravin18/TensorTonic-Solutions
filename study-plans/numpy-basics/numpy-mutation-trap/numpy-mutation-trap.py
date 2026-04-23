import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    data = np.asarray(data, dtype = np.float64)
    output = data[row_idx].copy()
    output = output.reshape(1,-1)
    output = np.vstack((output, np.clip(output, lo, hi)))
    return output