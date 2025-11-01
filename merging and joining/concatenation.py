# concat() to join
import pandas as pd
customers1=pd.DataFrame({
    "ID":[9,2,3],
    "name":['s','s','f']
})
customers2=pd.DataFrame({
    "ID":[1,7,5],
    "name":['l','k','z']
})
vertical=pd.concat([customers1,customers2],ignore_index=True)#default is vertical
horrizontal=pd.concat([customers1,customers2],axis=1,ignore_index=True)#default is vertical
print(vertical)
print(horrizontal)