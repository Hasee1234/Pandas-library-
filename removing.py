import pandas as pd
df=pd.read_csv("output.csv")

#remove one column or more
df.drop(columns=['salary'],inplace=True)
df.drop(columns=['salary','age'],inplace=True)
print(df)