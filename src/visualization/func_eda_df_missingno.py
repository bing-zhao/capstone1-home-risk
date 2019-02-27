# function to plot the missing values
def func_eda_df_missingno(df, prefix='', dir_png='../reports/figures/'):
    """function to plot the normalized probability density distribution colored by label
    Keyword arguments: df_X (feature dataframe), y (label pandas series), dir_png (output dir); Return: PNG files
    """

    import missingno as msno
    import matplotlib.pyplot as plt

    # missing value matrix
    # - missing value indicated by white regions
    # - the bar on the right indicae each row's data completeness (number of valid values in each row)
    plt.figure(figsize=[14,10])
    msno.matrix(df)
    pngname = dir_png+'eda-missingno-heatmap-'+prefix+'.png'
    print('Missing value heatmap saved at {}'.format(pngname))
    #plt.tight_layout()
    plt.savefig(pngname)

    # missing value correlation
    plt.figure(figsize=[14,8])
    msno.heatmap(df)  # Detailed housing characteristics
    pngname = dir_png+'eda-missingno-correlation-'+prefix+'.png'
    print('Missing value heatmap saved at {}'.format(pngname))
    plt.tight_layout()
    plt.savefig(pngname)

    return
