import numpy as np

def filter_and_extract(data, row_start, row_stop, threshold):
    """
    Returns: 1D ndarray of float64
    """
    data = np.asarray(data ,dtype = np.float64)
    data = data[row_start: row_stop]
    return data[data > threshold]