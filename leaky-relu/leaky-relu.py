import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    relu_output = [n if n > 0 else alpha * n for n in x] 
    return np.array(relu_output)