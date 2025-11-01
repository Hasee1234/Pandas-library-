# head() tail()
import pandas as pd

# import datasets
df = pd.read_csv("output.csv")

print("First 2 rows of the dataset:")
# print(df.head(2))  # Display first 5 rows

print("\nLast 3 rows of the dataset:")
# print(df.tail(3))  # Display last 5 rows

print(df.info())  # Display summary information about the DataFrame
print(df.describe())  # Display statistical summary of numerical columns
print(df.columns)  # Display column names
print(df.shape)  # Display the shape of the DataFrame (rows, columns)


#if you print single column it will give series 
print("single column data:",df['name'])  # Access a single column

#if you print multiple column it will give dataframe
print("multiple column data:\n",df[['name','age']])  # Access multiple

# # if you want specific rows with single condition
print("Rows where age > 25:\n",df[df['age'] > 25])  # Rows where age > 25

#if you print multiple column it will give series 
print("specific age and city people",df[(df['age'] > 25) & (df['salary'] > 9000)])  # Rows where age > 25 and city is 'c'
print("specific age and city people",df[(df['age'] > 25) | (df['salary'] > 9000)])  # Rows where age > 25 and city is 'c'
