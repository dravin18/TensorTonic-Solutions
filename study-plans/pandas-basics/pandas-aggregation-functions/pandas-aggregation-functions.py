import pandas as pd

def multi_agg(data, group_col, value_col, funcs):
    """
    Returns: dict mapping function name to {group: value} dict
    """
    df = pd.DataFrame(data)
    grouped = df.groupby(group_col)[value_col]
    agg_group = grouped.agg(funcs)
    result = agg_group.to_dict()
    return result