import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """
    result = []
    df = pd.DataFrame(data)
    df.set_index(index_col, inplace = True)
    result.append(df.columns.tolist())
    df.reset_index(inplace = True)
    result.append(df.columns.tolist())
    return result