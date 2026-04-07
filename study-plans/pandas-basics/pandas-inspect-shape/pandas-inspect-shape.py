import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    df = pd.DataFrame(data)
    row, col = df.shape
    dtype_dict = df.dtypes.to_dict()
    dtype_dict = {k : str(v) for k, v in dtype_dict.items()}
    output_dict = {'rows': row, 'cols' : col, 'columns': df.columns.to_list(), 'dtypes': dtype_dict, 'total_values': row * col}
    return output_dict