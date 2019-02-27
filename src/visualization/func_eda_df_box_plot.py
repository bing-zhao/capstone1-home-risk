# function to plot the normalized probability density distribution colored by label
def func_eda_df_box_plot(df_X, prefix='', figsize=(12,2), dir_png='../reports/figures/'):
    """function to plot box plots
    Keyword arguments: df_X (feature dataframe), Optional: prefix, figsize, dir_png (output dir); Return: PNG files
    """
    import numpy as np
    import matplotlib.pyplot as plt

    for col in df_X.columns:
        fig = plt.figure(figsize=figsize)
        plt.boxplot(df_X[col].dropna(), vert=False)
        plt.xlabel(col)
        plt.tight_layout()
        plt.savefig(dir_png+'eda-box-'+prefix+col+'.png')
        plt.close(fig)
        # plt.show()

    return
