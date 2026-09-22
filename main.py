import pandas as pd

#Load dataset
df = pd.read_csv("data_sets/House_Pricing.csv")

print(df.head())
print(df.describe())
print(df.info())
print(df.shape)

#Duplicate Removal
print(df.duplicated().sum()) #checking for duplocates in rows
print(df.T.duplicated().sum()) #checking for duplocates in rows

#Handling Missing Value
print(df.isna().sum())
