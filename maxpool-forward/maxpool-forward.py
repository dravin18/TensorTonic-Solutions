def maxpool_forward(X: list, pool_size: int, stride: int) -> list:
    """
    Returns the maximum value from every pooling window.
    """
    H = len(X)
    W = len(X[0])

    # Output dimensions must be integers
    H_out = ((H - pool_size) // stride) + 1
    W_out = ((W - pool_size) // stride) + 1

    # Create independent rows
    Out = [[float("-inf") for _ in range(W_out)] for _ in range(H_out)]

    for i in range(H_out):
        for j in range(W_out):
            for x in range(i * stride, i * stride + pool_size):
                for y in range(j * stride, j * stride + pool_size):
                    if Out[i][j] < X[x][y]:
                        Out[i][j] = X[x][y]

    return Out