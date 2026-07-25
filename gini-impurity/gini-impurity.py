from collections import Counter

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    total = len(y_left) + len(y_right)
    if total == 0:
        return 0.0
    ans = 0
    for item in (y_left, y_right):
        y_left_c = Counter(item)
        gini = 1
        for element, count in y_left_c.items():
            gini -= (count / len(item))**2
        ans += len(item) * gini / total
    return ans
    