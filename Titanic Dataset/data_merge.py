import pandas as pd

df1 = pd.read_csv('gender_submission.csv')
df2 = pd.read_csv('test.csv')
df3 = pd.read_csv('train.csv')

df_comb = df3.merge(df2, how= 'left').merge(df1, how='left')

df_comb.to_csv('merged_titanic_data.csv', index= False)