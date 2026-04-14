import numpy as np

def generate_random_array(shape, kind, seed):
    """
    Returns: 2D ndarray of float64 random values
    """
    # if kind == 'uniform':
    #     rng = np.random.default_rng(seed = seed)
    #     return rng.uniform(size = tuple(shape))
    # if kind == 'normal':
    #     rng = np.random.default_rng(seed = seed)
    #     return rng.normal( 0 , 1,  size = tuple(shape))

    if kind == 'uniform':
        rng = np.random.RandomState(seed)
        return rng.uniform(size=tuple(shape))
    if kind == 'normal':
        rng = np.random.RandomState(seed)
        return rng.normal(0, 1, size=tuple(shape))