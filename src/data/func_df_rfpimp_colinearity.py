# function to calculate the colinearity of features based on Spearman's rank-order correlation using rfpimp package
def func_df_rfpimp_colinearity(df, figsize=(7,5), pngname=''):
    """function to calculate the colinearity of features based on Spearman's rank-order correlation using rfpimp package
    Keyword arguments: df (dataframe of features), optional: figsize=(7,5), pngname=''; Return: df_feature_corr_matrix, plot of corr heatmap
    """
    #
    from rfpimp import feature_corr_matrix
    from rfpimp import plot_corr_heatmap
    df_feature_corr_matrix = feature_corr_matrix(df)
    viz = plot_corr_heatmap(df, figsize=figsize)
    if pngname:
        viz.save(pngname)
    return df_feature_corr_matrix
