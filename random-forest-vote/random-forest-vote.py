import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    pred = np.array(predictions)
    _, col = pred.shape
    class_list = []
    for index in range(0,col,1):
        pred_var = pred[:,index]
        uniq = np.unique_counts(pred_var)
        unique_class = uniq.values
        unique_counts = uniq.counts
        class_index = int(np.argmax(unique_counts))
        class_list.append(unique_class[class_index])
    return class_list