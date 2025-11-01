# fillna()
# to fill values 

import pandas as pd

data={
    "name":["x","j",None,"n"],
    "age":[24,25,None,27],
    "city":["a",None,"c","d"]
}
df=pd.DataFrame(data) 
print(df)

df.fillna(0,inplace=True)#to enter one value
print(df)
df['age'].fillna(df['age'].mean(),inplace=True)#fro specific column
print(df)
