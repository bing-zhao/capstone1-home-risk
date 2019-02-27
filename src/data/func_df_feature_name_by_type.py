# function classified features by their types
def func_df_feature_name_by_type(df):
    """function classified features by their types
    Keyword arguments: df (dataframe); Return: feature_dict (dictionary containing feature names by type)
    """
    numerical_features = list(df.select_dtypes(include = ['integer','float']).columns.values);
    print('Number of numerical features (inclusive of Binary): {}'.format(len(numerical_features)))

    # categorical features
    categorical_features = list(df.select_dtypes(include = ['object']).columns.values)
    print('Number of categorical features: {}'.format(len(categorical_features)))

    # binary numerical features (0, 1), need to check if all binary features are coded as 0,1
    binary_features = [col for col in df if
                   df[col].dropna().value_counts().index.isin([0,1]).all()]
    print('Number of binary features: {}'.format(len(binary_features)))

    # numerical features (exclude binary)
    numerical_features = [e for e in numerical_features if e not in binary_features]
    print('Number of numerical features (exclusive of Binary): {}'.format(len(numerical_features)))

    # save feature names into dictionary
    feature_dict = {'numerical_features': numerical_features,
                   'categorical_features': categorical_features,
                   'binary_features': binary_features}
    return feature_dict
