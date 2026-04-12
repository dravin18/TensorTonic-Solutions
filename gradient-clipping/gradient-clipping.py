import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    g = np.asarray(g, dtype = float)
    # g_mag = np.sqrt(np.sum(np.power(g, 2)))
    if max_norm <= 0:
        return g.copy()
    g_mag = np.linalg.norm(g)
    if g_mag <= max_norm or g_mag == 0:
        return g.copy()
    else:
        return g * (max_norm / g_mag)
        