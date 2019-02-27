import pandas as pd

def func_df_add_missing_flag(df, col_w_missing_values):
    '''function to add columns for missing value flags
    return: df (with additional binary columns, 0 and 1)
    '''

    for c in col_w_missing_values:

        df[c+'_na'] = pd.isnull(df[c]) * 1

    return df
