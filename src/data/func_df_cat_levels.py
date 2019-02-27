# function to print the levels of categorical variables
def func_df_cat_levels(df):
    """function to print the levels of categorical variables
    Keyword arguments: df (dataframe); Return: print unique levels
    """
    ### df = data frame with all categorical features
    import pandas as pd

    features = []
    level_num = []
    levels = []
    for name, col in df.items():
        features.append(name)
        level_num.append(df[name].nunique())
        levels.append(df[name].unique())
        #print('{} has {} levels: {}'.format(name,df[name].nunique(),df[name].unique()))
    df_cat = pd.DataFrame({'features': features, 'level_num':level_num, 'levels':levels})
    df_cat.sort_values(by='level_num',inplace=True)
    return df_cat
