## function to plot feature importance from a trained RandomForest model, and output importance in dataframe format
def func_rf_feature_importance(clf, features, figsize=(4,6), pngname=''):
    """function to plot feature importance from a trained RandomForest model, and output importance in dataframe format
    Keyword arguments: clf (rf classifier), features (list of names), Optional: figsize, pngname; Return: PNG file, df_fi
    """
    import matplotlib.pyplot as plt
    import numpy as np

    importances = clf.feature_importances_
    indices = np.argsort(importances)

    plt.figure(figsize=figsize)
    plt.title('Feature Importances')
    plt.barh(range(len(indices)), importances[indices], color='b', align='center')
    plt.yticks(range(len(indices)), [features[i] for i in indices])
    plt.xlabel('Relative Importance')
    plt.show()
    if pngname:
        plt.savefig(pngname)

    df_fi = pd.DataFrame({'feature': features,'importance': importances})
    df_fi.sort_values(by=['importance'], ascending=False, inplace=True)

    return df_fi
