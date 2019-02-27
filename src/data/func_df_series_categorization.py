# function to convert a string pandas series into categorical series
import pandas as pd
def func_df_series_categorization(df):
    """function to convert a string pandas series into categorical series
    Keyword arguments: df (one column dataframe); Return: label encoded value
    """
    ### convert a string pandas series into categorical series
    if not pd.api.types.is_numeric_dtype(df):
        label_name = df.name
        # convert to categorical
        df=df.to_frame(name=label_name).apply(lambda x: x.astype(pd.api.types.CategoricalDtype())) # need dataframe as input
        display(df.info()) # check the type
        # encoding
        df[label_name] = df[label_name].cat.codes.values
        df = df[label_name] # convert back to pandas series
    else:
        print('no need to covert. already numerical.')
    return df
