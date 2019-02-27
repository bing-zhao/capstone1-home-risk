# random forest: plot feature importance dataframe from rf_feat_importance
def func_rf_feature_importance_plot(df):
    """function to plot the feature importance of a random forest model
    Keyword arguments: df (feature importance df from func_rf_feature_importance); Return: plot
    """
    return fi.plot('feature', 'importance', 'barh', figsize=(12,7), legend=False)
