# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas",
# ]
# ///

# Day 26: Data Analysis with Pandas
import pandas as pd
# Filtering and selecting data
df = pd.read_csv("dirty_data.csv")
# print(df.head())
# print(df["Age"])
# print(df[["Age", "City", "Name"]])
# print(df[df["Age"] > 30].reset_index())
# print(df[df["Age"] > 30])
# print(df[(df['Age'] > 25) & (df['Salary'] > 50000) & (df["City"] == "New York")])
# print(df.query("Age > 30 and City == 'New York' and Salary > 50000"))
# print(df[df["Age"].between(25,30)])
# print(df[df["City"].isin(["Dhaka", "London"])])



# Groupby operations
# print(df.groupby("Gender").count())
# print(df.groupby("Gender")["Salary"].mean())
# print(df.groupby("City")["Salary"].mean())
# print(df.groupby(["City", "Gender"])["Salary"].mean())



# Sorting and aggregation

# print(df.groupby("City").agg({'Salary': ['mean', 'max', 'min']}))
# print(df["Salary"].sum())
# print(df["Salary"].mean())
# print(df["Salary"].max())
# print(df["Salary"].min())
# print(df["Age"].mean())
# print(df.agg({'Salary': ['sum', 'mean', 'max', 'min'], 'Age':['mean', 'max', 'min']}))

# Practice: Analyze sales data, student grade analysis
sdf = pd.read_csv("sales_data.csv")
stdf = pd.read_csv("student_grades.csv")

# print(sdf.groupby(["Category", "Profit"]).agg({'Sales': ['mean', 'min', 'max']}))
# print(stdf.groupby(["Gender", "Subject"]).agg({'Marks': ['mean', 'min', 'max']}))
print(stdf.groupby("Gender").count())
print(stdf[stdf["Marks"] > 80].groupby("Gender").count())