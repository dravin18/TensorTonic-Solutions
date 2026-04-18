import numpy as np
from collections import Counter

def knn_classify(X_train, y_train, X_test, k=3):
    """
    Returns: A list of predicted integer labels for each test point
    """
    X_train = np.asarray(X_train)
    y_train = np.asarray(y_train)
    X_test = np.asarray(X_test)
    row, column = X_test.shape

    output_label = []
    for i in range(0,row,1):
        item = X_test[i,:]
        distance = np.sqrt(np.sum((X_train - item)**2, axis = 1))
        indices = distance.argsort()[:k]
        d = Counter(y_train[indices].tolist())
        max_count = max(d.values())
        best_label = min(label for label, c in d.items() if c == max_count)
        output_label.append(best_label)

    return output_label
