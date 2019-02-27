# function to extend the display of jupyter-notebook
def func_df_display_all(df,max_rows=1000,max_cols=1000):
    """function similar to display, but temporarily extend the max number of rows and columns
    Keyword arguments: df (dataframe), max_rows, max_cols; Return: display
    """
    import pandas as pd
    ### display more info by extending max_rows, max_columns
    with pd.option_context("display.max_rows", max_rows, "display.max_columns", max_cols):
        display(df)
