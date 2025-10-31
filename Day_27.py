# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "matplotlib",
#     "pandas",
# ]
# ///

# Day 27: Data Visualization - Matplotlib
# Install Matplotlib

import matplotlib.pyplot as plt
import pandas as pd

# Line plots, bar charts, scatter plots

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temperature = [30, 32, 31, 29, 35]

plt.plot(days, temperature, color ="orange", marker = "o", ms = 20, mec="r" )
plt.title("Temperature Over the Days")
plt.xlabel("days")
plt.ylabel("temperature(c)")
plt.grid(True)
plt.show()





products = ['Laptop', 'Phone', 'Tablet', 'Monitor']
sales = [120, 150, 90, 60]

plt.bar(products, sales, color="Skyblue")
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Productions")
plt.show()




x = [10, 20, 30, 40, 50]
y = [15, 25, 45, 35, 55]


plt.scatter(x, y, color = "red")
plt.title("Scatter")
plt.xlabel("X label value")
plt.ylabel("y label value")
plt.show()
# Practice: Visualize temperature data, sales trends, grade distribution

grades = pd.read_csv("student_grades.csv")
plt.hist(grades['Marks'], bins=5, color='purple', edgecolor='black')
plt.title("Grade Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
