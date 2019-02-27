# function to return and print the data types of columns within a dataframe

def func_df_col_names_by_type(df, flag_print = False):
    """function to return and print the data types of columns within a dataframe
    Keyword arguments: df (dataframe), flag_print (default = False); Return: cols_dict (dictionary), cols_df (dataframe)
    """
    import pandas as pd
    # Identify binary cols
    numerical_cols = df.select_dtypes(include = ['number'], exclude = None).columns.tolist()
    # binary numerical cols (0, 1), need to check if all binary cols are coded as 0,1
    binary_cols = [col for col in df if df[col].dropna().value_counts().index.isin([0,1]).all()]
    # numerical cols (exclude binary)
    numerical_cols_exclude_binary = [e for e in numerical_cols if e not in binary_cols]
    # categorical cols (include binary)
    categorical_cols = df.select_dtypes(include = ['object'], exclude = None).columns.tolist()
    categorical_cols_include_binary = categorical_cols + binary_cols

    #  check through all data types using .select_dtypes()
    cols_dict = {
        "cols_number": numerical_cols,
        "cols_string": categorical_cols,
        "cols_binary": binary_cols,
        "cols_number_exclude_binary": numerical_cols_exclude_binary,
        "cols_string_include_binary": categorical_cols_include_binary,
        "cols_datetime": df.select_dtypes(include = ['datetime','datetime64'], exclude = None).columns.tolist(),
        "cols_timedelta": df.select_dtypes(include = ['timedelta','timedelta64'], exclude = None).columns.tolist(),
        "cols_category": df.select_dtypes(include = ['category'], exclude = None).columns.tolist(),
        "cols_others": df.select_dtypes(include = None,
                                            exclude = ['number','object','datetime','datetime64','timedelta','timedelta64','category']).columns.tolist()
    }

    # print all data type of all cols {col_type: col_name}
    if flag_print:
        for key,value in cols_dict.items():
            for v in value:
                print("{}:{}".format(key,v))

    # save to dataframe format
    feature_type = []
    feature_num = []
    feature_list = []
    for key,value in cols_dict.items():
        feature_type.append(key)
        feature_num.append(len(value))
        feature_list.append(value)
    cols_df = pd.DataFrame({'feature_type':feature_type, 'feature_num':feature_num, 'feature_list':feature_list})

    return cols_dict, cols_df
