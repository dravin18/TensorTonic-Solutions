import numpy as np
from collections import Counter

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    train_items = Counter(y_train)
    total_count = len(y_train)
    frac_counter = {k : v / total_count  for k, v in train_items.items()}
    
    mk = []
    mv = float('-inf')

    for k, v in frac_counter.items():
        if v >= mv:
            mv = v

    mk = [key for key, value in frac_counter.items() if value == mv]
    max_class = mk[0]
            
    output = [mk[0]] * len(X_test)
    return output