import pandas as pd
#to sort use sort_vlues() method
data={
    "name":["x","j",None,"n"],
    "age":[32,30,24,27],
    "city":["a",None,"c","d"],
    "salary":[7,84,846,53]
}
df=pd.DataFrame(data)
df.sort_values(by='age',ascending=False,inplace=True)
print("age in descending order")
print(df)

# also more than one column can be sorted once 
df.sort_values(by=['age','salary'],ascending=[False,True],inplace=True)
print(df)


# SUMMARY 
max=df['age'].max()
min=df['age'].min()
average=df['age'].mean()
print(max,min,average)