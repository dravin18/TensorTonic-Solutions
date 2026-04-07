import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    df = pd.DataFrame(data)
    output_dict = { 'values' : df[column].to_list(), 'length' : len(df[column].to_list())}
    return output_dict