def func_stat_cramers_v(x,y):
    import pandas as pd
    from scipy import stats
    confusion_matrix = pd.crosstab(index = x,
                                   columns = y,
                                   margins = True)
    chi2 = stats.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2/n
    r,k = confusion_matrix.shape
    phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
    rcorr = r-((r-1)**2)/(n-1)
    kcorr = k-((k-1)**2)/(n-1)
    return np.sqrt(phi2corr/min((kcorr-1),(rcorr-1)))

def func_df_cramers_v(dfx,dfy):
    cramers_v_vals = []
    for col in dfx.columns:
        cramers_v_val = func_stat_cramers_v(dfx[col],dfy)
        cramers_v_vals.append(cramers_v_val)
        #print("{}: {:.4f}".format(col,cramers_v_val))

    df_crmaers_v = pd.DataFrame({'feature': dfx.columns,'cramers_v': cramers_v_vals})
    df_crmaers_v.sort_values(by=['cramers_v'], ascending=False, inplace=True)
    return df_crmaers_v

# The functions below have not been cleaned up yet. 
# Goodman-Kruskal Lambda for Nominal-Nominal Correlation
def goodman_kruskal(x):
    temp = pd.crosstab(index = df_Deliverability_BIFs_sub[cols_X[x]],
                       columns = df_Deliverability_BIFs_sub['dr_attempt_status'],
                       margins = True)

    store = 0

    for i in range(len(temp) - 1):
        if temp[0][i] < temp[1][i]:
            store += temp[0][i]
        else:
            store += temp[1][i]

    sumOfZeros = 0
    sumOfOnes = 0

    for i in range(len(temp) - 1):
        sumOfZeros += temp[0][i]
        sumOfOnes += temp[1][i]

    if sumOfZeros < sumOfOnes:
        GK = 1- store/sumOfZeros
    else:
        GK = 1- store/sumOfOnes
    return GK

# 8 6 9 0 7 10 1 2 4
print ('activity_date_Hour:', goodman_kruskal(8)) # answer should be 0.061480718280836
print ('activity_date_Month:', goodman_kruskal(6))
print ('dst_bundle_name_cat:', goodman_kruskal(9))
print ('dst_bundle_name:', goodman_kruskal(0))
print ('activity_date_DayofWeek:', goodman_kruskal(7))
print ('src_bundle_name_cat:', goodman_kruskal(10))
print ('src_bundle_name:', goodman_kruskal(1))
print ('dr_final_cat:', goodman_kruskal(2))
print ('bundle_delivery_type:', goodman_kruskal(4))

# the rest have 0.0 because number of '1's is more dominant than '0's in all categories




import math

def pearson_contingencyCoeff(x):
    obs = pd.crosstab(index = df_Deliverability_BIFs_sub[cols_X[x]],
                       columns = df_Deliverability_BIFs_sub['dr_attempt_status'],
                       margins = True)

    col1Sum = 0
    col2Sum = 0
    rowSum = []

    for i in range(len(obs)):
        col1Sum += obs[0][i]
        col2Sum += obs[1][i]
        rowSum.append(obs[0][i] + obs[1][i])

    temp = col1Sum + col2Sum
    expectedCol1 = []
    expectedCol2 = []

    for i in range(len(obs)):
        expectedCol1.append(col1Sum*rowSum[i]/temp)
        expectedCol2.append(col2Sum*rowSum[i]/temp)

    finalCol1 = []
    finalCol2 = []

    for i in range(len(obs)):
        finalCol1.append(((expectedCol1[i]-obs[0][i])**2)/expectedCol1[i])
        finalCol2.append(((expectedCol2[i]-obs[1][i])**2)/expectedCol2[i])

    chisq = 0

    for i in range(len(obs)):
        chisq += finalCol1[i]
        chisq += finalCol2[i]

    return math.sqrt(chisq/(temp + chisq))




#Phi Coefficient for Nominal-Nominal Correlation
from sklearn.metrics import matthews_corrcoef

def phi_coeff(x):
    a = []
    b = []

    for i in df_Deliverability_BIFs_sub[cols_X[x]]:
        a.append(i)

    for i in df_Deliverability_BIFs_sub['dr_attempt_status']:
        b.append(i)

    return matthews_corrcoef(a,b)


# Point Biserial for Quantitative-Nominal Correlation
from scipy import stats

def point_biserial(x):
    a = []
    b = []

    for i in df_Deliverability_BIFs_sub[cols_X[x]]:
        a.append(i)

    for i in df_Deliverability_BIFs_sub['dr_attempt_status']:
        b.append(i)

    # len(a) = 492537
    # len(b) = 492537

    return stats.pointbiserialr(a,b)
