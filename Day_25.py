# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas",
# ]
# ///
# Day 25: Introduction to Pandas
# Install Pandas
import pandas as pd
# Series and DataFrames
# a = pd.Series([1,2,3,4,5,6,7,8,9])
# data = {
#     "name": ["m","o","s","t","a"],
#     "age": [20,25,23,24,26] 
# }
# d = pd.DataFrame(data)
# print(d.loc[0])


# Basic operations: head(), info(), describe()
# Reading CSV files
# df =pd.read_csv("heart.csv")
# print(df.head(10))
# print(df.info())
# print(df.describe())
# Practice: Load and explore a dataset, basic data cleaning
df = pd.read_csv("dirty_data.csv")
# print(df.describe())
# print(df.head())
# print(df.info())
print(df.isnull().sum())
print(df.isna().sum())
# print(df.notnull())
dropna = df.dropna()
df.replace({'Male': 1, 'Female': 0}, inplace=True)  
fle = df.fillna(0)
fileMeanValu = df["Gender"].fillna(df["Gender"].mean(), inplace=True)
df.sort_values(by="Age")
print(df[df["Age"] > 25])