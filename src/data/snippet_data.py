# # EDA

# list feature names except
features= [c for c in df.columns.values if c not in ['feature_to_exclude']]

# list the number of factors within each categorical variable
df[list(df_raw.select_dtypes(include = ['object']).columns.values)].apply(pd.Series.nunique, axis = 0)

# plot the histogram of a feature, colored by y
plt.figure(figsize=(12,12))
ax = sns.countplot(y='x', hue='y', data=df_raw)

# map two level categorical feature into binary
m = {'m' : 1, 'f' : 0}
df['gender'] = df['gender'].str[0].str.lower().map(m)
