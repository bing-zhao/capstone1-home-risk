from rfpimp import feature_dependence_matrix
from rfpimp import plot_dependence_heatmap
from sklearn.ensemble import RandomForestClassifier

# function to derive the feature dependence based on simple randomforest model and permutation importance based on oob_score using rfpimp package
def func_df_rfpimp_feature_dependence(df, rfmodel=RandomForestClassifier(n_estimators=50, oob_score=True), figsize=(7,5), pngname=''):
    """function to derive the feature dependence based on simple randomforest model and permutation importance based on oob_score using rfpimp package
    Keyword arguments: df (dataframe of features), optional: rfmodel, figsize=(7,5), pngname=''; Return: df_dep, plot of heatmap
    """
    # use rfpimp package
    df_dep = feature_dependence_matrix(df,
                                       rfmodel=rfmodel)
    # using all default settings:
    # n_samples=5000
    # rfmodel=RandomForestRegressor(n_estimators=50, oob_score=True)

    viz = plot_dependence_heatmap(df_dep, figsize=figsize)
    if pngname:
        viz.save(pngname)
    return df_dep
