import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """
    output_dict = {}
    df = pd.DataFrame(data)
    columns_list = df.columns.to_list()
    data_dict = {}
    for column in columns_list:
        data_dict.update({column : df[column].to_list()})
    output_dict.update({'data' : data_dict})
    x, y = df.shape
    output_dict.update({'shape' : [x, y]})
    output_dict.update({'columns': columns_list})
    return output_dict