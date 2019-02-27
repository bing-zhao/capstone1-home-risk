import pandas as pd
import matplotlib.pyplot as plt

# function to examine the frequency and response level within a categorical variable
def func_cat_crosstab(df_X, y_binary, sortby='Frequency'):
    """function to examine the frequency and response level within a categorical variable
    Keyword arguments: df_X (a categorical feature), y_binary (label with 1/0), sortby='Frequency'/'Response_Rate'; Return: df_ct (crosstab dataframe), plot Frequency vs Response
    """

    df_ct = pd.crosstab(df_X, y_binary, margins=False)
    df_ct['Count'] = df_ct.sum(axis=1)
    df_ct['Frequency'] = df_ct['Count']/df_ct['Count'].sum()*100
    df_ct['Frequnecy'] = df_ct['Frequency'].round(decimals=2)
    df_ct['Response_Rate'] =df_ct[1]/df_ct['Count']*100
    df_ct['Response_Rate'] = df_ct['Response_Rate'].round(decimals=2)
    df_ct = df_ct.sort_values(by=sortby,ascending=False)
    df_ct['Frequnecy_Cumu'] = df_ct['Frequnecy'].cumsum()
    plt.figure()
    plt.scatter(df_ct['Frequnecy'],df_ct['Response_Rate'])
    plt.xlabel('Frequency')
    plt.ylabel('Response Rate')
    plt.tight_layout()
    plt.show()
    return df_ct
