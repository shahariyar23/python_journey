# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas",
#      "matplotlib"
# ]
# ///
# Day 30: Mini Project - Part 2 & Review
# Complete your mini project
# Add error handling and documentation
# Upload in GitHub
import os 
import pandas as pd
import datetime
import matplotlib.pyplot as plt

# ---------- Add Expense ----------
def addExpense(date, category, amount, note):
    try:
        if os.path.exists("expense.csv"):
            df = pd.read_csv("expense.csv")
        else:
            df = pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])

        newRow = {"Date": date, "Category": category, "Amount": amount, "Note": note}
        df = pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)
        df.to_csv("expense.csv", index=False)
        print(" Expense added successfully.\n")

    except Exception as e:
        print(f" Error adding expense: {e}")


# ---------- View Expenses ----------
def viewExpense():
    try:
        if not os.path.exists("expense.csv"):
            print(" No expense file found.")
            return
        df = pd.read_csv("expense.csv")
        print(df.to_string(index=True))
    except Exception as e:
        print(f" Error viewing expenses: {e}")


# ---------- Modify Expense ----------
def modifyExpense(category=None, amount=None, note=None):
    try:
        if not os.path.exists("expense.csv"):
            print(" No expense file found.")
            return

        df = pd.read_csv("expense.csv")
        print(df)
        index = int(input("Enter the serial number to modify: "))

        if index < 0 or index >= len(df):
            print(" Invalid index.")
            return

        if category:
            df.loc[index, "Category"] = category
        if amount:
            df.loc[index, "Amount"] = amount
        if note:
            df.loc[index, "Note"] = note

        df.loc[index, "Date"] = datetime.date.today()
        df.to_csv("expense.csv", index=False)
        print(" Expense updated successfully!\n")

    except ValueError:
        print(" Invalid input type. Please enter valid data.")
    except Exception as e:
        print(f" Error modifying expense: {e}")


# ---------- Delete Expense by Index ----------
def deleteExpense():
    try:
        if not os.path.exists("expense.csv"):
            print(" No expense file found.")
            return

        df = pd.read_csv("expense.csv")
        print(df)
        index = int(input("Enter the serial number to delete: "))

        if index < 0 or index >= len(df):
            print(" Invalid index.")
            return

        df = df.drop(index).reset_index(drop=True)
        df.to_csv("expense.csv", index=False)
        print(" Expense deleted successfully!\n")

    except ValueError:
        print(" Invalid input type. Please enter a valid number.")
    except Exception as e:
        print(f" Error deleting expense: {e}")


# ---------- Delete by Category ----------
def deleteByCategory(category=None):
    try:
        if not os.path.exists("expense.csv"):
            print(" No expense file found.")
            return

        df = pd.read_csv("expense.csv")

        if category:
            before = len(df)
            df = df[df["Category"].str.lower() != category.lower()]
            after = len(df)
            df.to_csv("expense.csv", index=False)
            print(f" Deleted {before - after} records of category '{category}'.\n")
        else:
            print(" Please provide a category name.")

    except Exception as e:
        print(f" Error deleting by category: {e}")


# ---------- Filter ----------
def filter(category=None, amount=None, note=None):
    try:
        if not os.path.exists("expense.csv"):
            print(" No expense file found.")
            return

        df = pd.read_csv("expense.csv")
        filtered_df = df.copy()

        if category:
            filtered_df = filtered_df[filtered_df["Category"].str.lower() == category.lower()]
        if amount:
            filtered_df = filtered_df[filtered_df["Amount"] == amount]
        if note:
            filtered_df = filtered_df[filtered_df["Note"].str.lower() == note.lower()]

        if filtered_df.empty:
            print(" No matching records found.\n")
        else:
            print("\nFiltered Expenses:\n")
            print(filtered_df.to_string(index=False))

    except Exception as e:
        print(f" Error filtering expenses: {e}")


# ---------- Total Expense ----------
def totalExpense():
    try:
        if not os.path.exists("expense.csv"):
            print(" No expense file found.")
            return

        df = pd.read_csv("expense.csv")
        total = df["Amount"].sum()
        print(f"\n Total Expense: {total}\n")

    except Exception as e:
        print(f" Error calculating total: {e}")


# ---------- Data Analysis ----------
def dataAnalize():
    try:
        if not os.path.exists("expense.csv"):
            print(" No expense file found.")
            return

        df = pd.read_csv("expense.csv")

        # --- Category Chart ---
        category_sum = df.groupby("Category")["Amount"].sum()
        category_sum.plot(kind="bar", color="teal")
        plt.title("Expenses by Category")
        plt.ylabel("Amount")
        plt.show()

        # --- Daily Chart ---
        df["Date"] = pd.to_datetime(df["Date"])
        daily_sum = df.groupby("Date")["Amount"].sum()
        daily_sum.plot(kind="line", marker="o", color="orange")
        plt.title("Daily Expense Trend")
        plt.ylabel("Amount")
        plt.show()

    except Exception as e:
        print(f" Error analyzing data: {e}")


# ---------- Main Menu ----------
while True:
    print("\n========= Expense Tracker =========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter Expenses")
    print("4. Total Expenses")
    print("5. Update Expense")
    print("6. Delete Expense by ID")
    print("7. Delete Expense by Category")
    print("8. Show Charts")
    print("9. Exit")
    print("==================================")

    choice = input("Choose an option: ")

    try:
        if choice == "1":
            date = datetime.date.today()
            category = input("Enter category: ").strip()
            amount = float(input("Enter amount: "))
            note = input("Enter short note: ").strip()
            addExpense(date, category, amount, note)

        elif choice == "2":
            viewExpense()

        elif choice == "3":
            print("Leave blank if you don’t want to filter that field.")
            category = input("Filter by category: ").strip() or None
            note = input("Filter by note: ").strip() or None
            amt = input("Filter by amount: ").strip()
            amount = float(amt) if amt else None
            filter(category, amount, note)

        elif choice == "4":
            totalExpense()

        elif choice == "5":
            viewExpense()
            category = input("New category (press enter to skip): ").strip() or None
            amt = input("New amount (press enter to skip): ").strip()
            amount = float(amt) if amt else None
            note = input("New note (press enter to skip): ").strip() or None
            modifyExpense(category, amount, note)

        elif choice == "6":
            deleteExpense()

        elif choice == "7":
            category = input("Enter category to delete: ").strip()
            deleteByCategory(category)

        elif choice == "8":
            dataAnalize()

        elif choice == "9":
            print(" Exiting Expense Tracker. Goodbye!")
            break

        else:
            print(" Invalid choice. Please select between 1–9.")

    except Exception as e:
        print(f"Unexpected error: {e}")