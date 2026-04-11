import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    frames = []
    for item in dfs:
        frames.append(pd.DataFrame(item))
    df_final = pd.concat(frames).reset_index(drop = True)
    return [list(df_final.shape),df_final.to_dict('list')]