def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    He = math.sqrt(6 / fan_in)
    return [[W[i][j] * 2 * He - He for j in range(len(W[0]))] for i in range(len(W))]