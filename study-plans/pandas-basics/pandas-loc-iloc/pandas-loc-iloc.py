import pandas as pd

def iloc_selection(data, row, col):
    """
    Returns: list [element, row_values, col_values]
    """
    df = pd.DataFrame(data)
    result = []
    result.append(df.iloc[row, col])
    result.append(df.iloc[row].to_list())
    result.append(df.iloc[:, col].to_list())
    return result