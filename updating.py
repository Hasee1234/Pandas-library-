import pandas as pd
df=pd.read_csv("output.csv")

#for updation single value
#df.loc[row_indexer,col_indexer]=new_value
df.loc[2,'age']=30  #updating age of index 2 to 30
print(df)

#fro updation more all values
df['salary']=df['salary']*1.5
print(df)