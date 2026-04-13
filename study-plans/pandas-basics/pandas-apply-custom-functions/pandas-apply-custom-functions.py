import pandas as pd

def apply_transform(data, column, operation):
    """
    Returns: dict with original columns plus column_transformed
    """
    df = pd.DataFrame(data)
    if operation == 'normalize':
        min_val = df[column].min()
        max_val = df[column].max()
        df[column + '_transformed'] = df[column].apply(lambda x : round((x - min_val)/(max_val - min_val),4))
    elif operation == 'rank':
        df[column + '_transformed'] = df[column].rank()
    elif operation == 'cumsum':
        df[column + '_transformed'] = df[column].cumsum()
    else:
        df[column + '_transformed'] = df[column].apply(lambda x : 2 * x)
    return df.to_dict('list')

        
    

        