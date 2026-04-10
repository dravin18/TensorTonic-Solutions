import pandas as pd

def merge_dataframes(left, right, on, how):
    """
    Returns: dict of column to value lists
    """
    l_df = pd.DataFrame(left)
    r_df = pd.DataFrame(right)
    df = pd.merge(l_df, r_df, on = on, how = how)
    return df.to_dict('list')