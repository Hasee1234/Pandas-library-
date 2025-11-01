#pd.merge(df1,df2,on=col_name,how="type of join")
import pandas as pd
customers1=pd.DataFrame({
    "ID":[1,2,3],
    "name":['s','s','f']
})
customers2=pd.DataFrame({
    "ID":[1,2,5],
    "salary":[1,23,45]
})
merge=pd.merge(customers1,customers2,on='ID',how="inner")#inner means print only matching values
merge=pd.merge(customers1,customers2,on='ID',how="outer")#outer means print all and those not having values give nan
merge=pd.merge(customers1,customers2,on='ID',how="right")
merge=pd.merge(customers1,customers2,on='ID',how="left")
merge=pd.merge(customers1,customers2,on='ID',how="cross")#m*n
print(merge)