import pandas as pd

def melt_dataframe(data, id_vars, value_vars):
    """
    Returns: dict with keys from id_vars plus 'variable' and 'value'
    """
    df = pd.DataFrame(data)
    return pd.melt(df, id_vars, value_vars, 'variable', 'value').to_dict('list')