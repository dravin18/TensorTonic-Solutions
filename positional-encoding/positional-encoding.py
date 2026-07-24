import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    pos_vector = np.arange(seq_len)[:, None]                     # (seq_len, 1)

    half_dim = (d_model + 1) // 2
    div_term = np.power(base, 2 * np.arange(half_dim) / d_model) # (half_dim,)
    angles = pos_vector / div_term                               # (seq_len, half_dim)

    pe = np.zeros((seq_len, d_model))

    pe[:, 0::2] = np.sin(angles)
    pe[:, 1::2] = np.cos(angles[:, :d_model // 2])

    return pe