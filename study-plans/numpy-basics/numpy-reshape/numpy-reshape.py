import numpy as np

def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """
    array_data = np.asarray(data, dtype = np.float64)
    if operation == 'flatten':
        return array_data.flatten()

    if operation == 'transpose':
        return array_data.T

    if operation == 'add_batch':
        return np.expand_dims(array_data, axis = 0)