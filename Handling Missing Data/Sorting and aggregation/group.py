import pandas as pd

data={
    "name":["x","j","n","e","e"],
    "age":[24,25,27,34,66],
    "city":["a","c","d","f","h"],
    "salary":[2000,3000,4000,1000,4000]
}
df=pd.DataFrame(data)

grouped=df.groupby("age")["salary"].sum()#to calculate salary of all ages so grouping salary n base of age
print(grouped)


multi=df.groupby(["age","name"])["salary"].sum()#to calculate salary of all ages so grouping salary n base of age and name

print(multi)