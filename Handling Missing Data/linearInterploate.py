import pandas as pd

data={
    "time":[1,2,3,4,5,6,7],
    "Value":[10,20,30,None,50,None,70]
}
#interpolate is a method to fillout missing values by estimation of its neigbouring values
df=pd.DataFrame(data)
print("before interpolate")
print(df)
df["Value"]=df["Value"].interpolate(methods="linear")
print("after interpolate")
print(df)

#use interploatio  in 1. timer series data   2.numeric data with trends     3. avoid dropping rows