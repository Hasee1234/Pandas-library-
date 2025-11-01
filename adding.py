import pandas as pd

df=pd.read_csv("output.csv")  
print(df)
#now to add new columns like here we will add bonus column
df['bonus']=(df["salary"]*0.1)
print(df)

#using insert method to add new column at specific location
#df.insert(loc,"col nmae",data)
df.insert(0,"department",["hr","it","sales","marketing"])
print(df)