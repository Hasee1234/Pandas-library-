import pandas as pd

data={
    "name":["x","j","z","n"],
    "age":[24,25,26,27],
    "city":["a","b","c","d"]
}

df =pd.DataFrame(data)
df.to_csv("output.csv",index=False)  #to save dataframe as csv file ,index false is used to avoid index column in csv file
df.to_json("output.json",orient="records")  #to save dataframe as json file , orient records is used to save each row as a separate json object
df.to_excel("output.xlsx",index=False)  #to save dataframe as excel file ,index false is used to avoid index column in excel file