# function similar to describe() with missing value
def func_df_describe_all(df): ## input a dataframe
    """function similar to describe() with missing value
    Keyword arguments: df (dataframe); Return: df_summary
    """
    df_summary = df.describe(include='all').T
    df_summary['miss_perc'] = (df.isnull().sum()/df.shape[0]*100).values
    return df_summary
