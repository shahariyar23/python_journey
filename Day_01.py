# variable 
# variable must start with a latter or the underscore 
x = 5
n = 3.45
age = 20
# snake case
my_name = "Mostak Shahariyar "
# camel case
myNama = "Mostak Shahariyr"
# pascal case
MyName = "Mostak Shahariyar"
fruits = ['Mango', 'apple', 'orange']
m,a, o = fruits
# or we can also write 
b, c, s = "banana", "Cherry", "strawberry"
# global variable: outside on the function we declear a variable is global or we can declear inside a function using global keyword like
def main():
    global age
    age = 21

# --------------------------------------------------

# print()
# print(x,n)
# print(my_name + myNama)
# print(m,a,o)
# print(b,c,s)
# print(age)


# input()
# id=input('Enter your id: ')
# print(f"your id is {id}") #here using f string

# comments
"""
here we already see the in line comments. now we see here multiple line comments
"""
# --------------------------------------------------
# data types

# text type: str
text = "this is a string"
# Numeric Types:	int, float, complex
nI = 10
nF= 20.5
nC = 10j
# Sequence Types:	list, tuple, range
fruitsList = ["apple", "banana", "strawberry"]
fruitsTuple = ("apple", "banana", "strawberry")
numRange = range(0,6)  # it means 0,1,2,3,4,5 output as a list

# Mapping Type:	dict
nameDict = {"name": "Mostak Shahariyar", "ID": 22203208, "Dept.": "CSE"}
# Set Types:	set
nameSet = {"name":"Mostak", "ID":22203208}
# Boolean Type:	bool
xBoolean = True



# Write programs for name printing, age calculator, and simple arithmetic
import datetime
def day_01():
    name = input("Enter your name: ")
    year = input("Enter your birh year: ")
    print("Enter 2 numner for addintion: ")
    n1 = input()
    n2 = input()
    # print(datetime.date.today())
    print(f"Name: {name} Age: {datetime.date.today().year - int(year)}  Addition Operation {n1} + {n2} = { int(n1) + int(n2) }")

if __name__ == "__main__":
    day_01()


