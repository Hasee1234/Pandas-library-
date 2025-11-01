# dropna() method to drop coljmns or row if you dont need


import pandas as pd

data={
    "name":["x","j",None,"n"],
    "age":[24,25,None,27],
    "city":["a",None,"c","d"]
}
df=pd.DataFrame(data)
print(df.isnull)#to identify null values
print(df.isnull().sum)#to identify number of null values


df.dropna(axis=0,inplace= True)#axis=0 means row and aXIS=1 MEANS COLJUMN
print(df)