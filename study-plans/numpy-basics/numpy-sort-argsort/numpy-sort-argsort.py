import numpy as np

def sort_with_indices(data, axis):
    """Returns: np.ndarray of shape (2, m, n), stacked sorted values and sort indices"""
    data = np.asarray(data, dtype = np.float64)
    sorted = np.sort(data, axis = axis)
    arg_sorted = np.argsort(data, axis = axis)
    r, c = data.shape
    output = np.zeros((2, r,c))
    output[0, :, :] = sorted
    output[1, :, :] = arg_sorted
    return output