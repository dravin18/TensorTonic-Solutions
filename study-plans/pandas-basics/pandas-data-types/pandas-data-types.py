import pandas as pd
from collections import Counter

def data_types_overview(data):
    """
    Returns: dict with 'dtypes', 'type_counts', 'num_columns'
    """
    df = pd.DataFrame(data)
    dtype_dict = df.dtypes.to_dict()
    dtype_dict = {k : str(v) for k, v in dtype_dict.items()}
    dtype_count = Counter(list(dtype_dict.values()))
    req_dict = {'dtypes' : dtype_dict, 'type_counts' : dtype_count, 'num_columns' : sum(dtype_count.values())}
    return req_dict