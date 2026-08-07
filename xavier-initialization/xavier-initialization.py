def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    X_b = (6 / (fan_out + fan_in))**(1/2)
    cols = len(W[0])
    rows = len(W)
    for row in range(rows):
        for col in range(cols):
            W[row][col] = W[row][col] * (2 * X_b) - X_b
    return W