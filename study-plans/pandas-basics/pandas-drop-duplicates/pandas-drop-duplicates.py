import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    result = []
    df = pd.DataFrame(data)
    result.append(len(df))
    df.drop_duplicates(inplace = True)
    result.append(len(df))
    result.append(df.to_dict('list'))
    return result