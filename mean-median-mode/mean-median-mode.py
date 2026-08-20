import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x)
    mean_x = np.mean(x)
    median_x = np.median(x)
    count_x = Counter(x)
    max_count = max(count_x.values())
    modes = [val for val,count in count_x.items() if count == max_count]
    return float(mean_x), float(median_x), float(min(modes))
    