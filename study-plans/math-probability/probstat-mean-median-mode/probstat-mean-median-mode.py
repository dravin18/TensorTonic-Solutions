import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    x = np.asarray(x, dtype = np.float64)
    count_x = Counter(x)
    return {'mean' : np.mean(x), 'median' : np.median(x), 'mode' : float(max(count_x, key=count_x.get)) }