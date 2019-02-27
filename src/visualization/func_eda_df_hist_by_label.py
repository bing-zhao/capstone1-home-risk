# function to plot the normalized probability density distribution colored by label
def func_eda_df_hist_by_label(df_X, Y, normal=False, figsize=(8,6), prefix='', dir_png='../reports/figures/'):
    """function to plot the normalized probability density distribution colored by label
    Keyword arguments: df_X (feature dataframe), y (label pandas series), normal(density plot), dir_png (output dir); Return: PNG files
    """
    import numpy as np
    import matplotlib.pyplot as plt

    y_uniques = Y.unique()  # unique labels, e.g. 0 or 1

    for col in df_X.columns:
        # filter nan vales
        mask = ~df_X[col].isnull()
        x = df_X.loc[mask, col]
        y = Y[mask]

        # plot
        fig = plt.figure(figsize=figsize)
        plt.hist([x[y == y_unique] for y_unique in y_uniques],
                 label=y_uniques,
                 weights=[np.ones(x[y == y_unique].count()) / x[y == y_unique].count() for y_unique in y_uniques])#density=True)
        plt.xlabel(col)
        plt.ylabel('Normalized Probability Distribution')
        plt.legend()
        plt.tight_layout()
        plt.savefig(dir_png+'eda-hist-'+prefix+col+'.png')
        plt.close(fig)
        # plt.show()

    return
