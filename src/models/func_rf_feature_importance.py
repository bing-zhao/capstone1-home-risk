# random forest feature importance: model, dataframe
def func_rf_feature_importance(m, df):
    """function to summarize the feature importance of a random forest model
    Keyword arguments: m (rf model), df (dataframe); Return: df['feature','importance'] in descending order
    """
    return pd.DataFrame({'feature':df.columns, 'importance':m.feature_importances_}
                       ).sort_values('importance', ascending=False)
