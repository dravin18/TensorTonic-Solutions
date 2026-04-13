import pandas as pd

def unstack_to_wide(data, index_col, columns_col, values_col):
    """
    Returns: dict with index_col plus one key per unique value in columns_col
    """
    df = pd.DataFrame(data)
    output_dict = pd.pivot(df, index = index_col, columns = columns_col, values =values_col).reset_index().to_dict('list')
    # output_dict = pd.crosstab(df, df[index_col], df[columns_col], df[values_col], aggfunc = 'sum').reset_index().to_dict('list')
    return output_dict