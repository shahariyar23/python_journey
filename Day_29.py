# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas",
#      "matplotlib"
# ]
# ///

# Day 29: Mini Project - Part 1
# Choose one project and start building:
# Expense Tracker with data visualization

import os 
import pandas as pd
import datetime
import matplotlib.pyplot as plt

def addExpense(date, category, amount, note):
    if os.path.exists("expense.csv"):
        df = pd.read_csv("expense.csv")
    else:
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])
    newRow = {"Date": date, "Category": category, "Amount": amount, "Note": note}
    newRowDf = pd.DataFrame([newRow])
    df = pd.concat([df, newRowDf], ignore_index= True)
    df.to_csv("expense.csv", index = False)
    print("Expense added successfully")
    
def viewExpense():
    df = pd.read_csv("expense.csv")
    print(df.to_string())


    
def filterByCategory(category):
    df = pd.read_csv("expense.csv")
    print(df[df["Category"] == category])
    
def totalExpense():
    df = pd.read_csv("expense.csv")
    print(f"Total expense: {df["Amount"].sum()}")
    

def dataAnalize():
    df = pd.read_csv("expense.csv")
    category_sum = df.groupby("Category")["Amount"].sum()
    category_sum.plot(kind="bar", color="teal")
    plt.title("Expenses by Category")
    plt.ylabel("Amount")
    plt.show()
    
    df['Date'] = pd.to_datetime(df['Date'])
    daily_sum = df.groupby('Date')['Amount'].sum()
    daily_sum.plot(kind='line', marker='o', color='orange')
    plt.title("Daily Expenses Trend")
    plt.ylabel("Amount")
    plt.show()


while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter by Category")
    print("4. Total Expenses")
    print("5. Show Charts")
    print("6. Exit")
    
    choice = input("Choose option: ")
    if choice == "1":
       print("Frist enter category, amount, and small note. \n Like Food 120 lunch")
       date = datetime.date.today()
       category = input("Enter the category: ")
       amount = int(input("Enter the amount: "))
       note = input("Enter one short note: ")
       addExpense(date, category, amount, note)
    elif choice == "2":
        viewExpense()
    elif choice == "3":
        print("Here you can filter your expense by category. \nLike food, transport, entertainment...")
        category = input("Enter the filetered categroy: ")
        filterByCategory(category)
    elif choice == "4":
        totalExpense()
    elif choice == "5":
        dataAnalize()
    elif choice == "6":
        break
