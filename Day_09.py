# Day 9: Functions - Part 2
# Default arguments

def oneFn(n=1):
    return n*5

# print(oneFn())

# *args and **kwargs

def argsFn(*x):
    for i in x:
        print(i)
# argsFn(1,2,3,5)
def kwargsFn(**x):
    print(x["name"])

# kwargsFn(name="mostak", l="shahariyar")

# Lambda functions
# lambda argument : expression

x = lambda a: a*5
# print(x(5))

# Map, filter, reduce
# map works as a loop or iterative 
n=[1,2,3,4,5,6]
# print(list(map(lambda a: a*2, n)))
# print(list(filter(lambda a: a % 2 == 0, n)))
# print(list(sorted(n)))
from functools import reduce
# print(reduce(lambda x,y: x+ y, n))



# Practice: List processor with lambda, flexible calculator

odd_number_squer_root = list(map(lambda a: a ** 2, filter(lambda a: a % 2 != 0, n)))
# print(odd_number_squer_root)
even_number_sum = reduce(lambda a, b: a + b, filter(lambda a: a % 2 == 0, n))
# print(even_number_sum)

# flexible calculator
add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b

def calculator():
    cal = input("Which operation you do add, sub, mul, div: ")
    if cal.lower() == "add" or "+":
        n1 = int(input("Enter one number: "))
        n2 = int(input("Enter one number: "))
        print(add(n1, n2))
    if cal.lower() == "sub" or "-":
        n1 = int(input("Enter one number: "))
        n2 = int(input("Enter one number: "))
        print(sub(n1, n2))
    if cal.lower() == "mul" or "*":
        n1 = int(input("Enter one number: "))
        n2 = int(input("Enter one number: "))
        print(mul(n1, n2))
    if cal.lower() == "div" or "/":
        n1 = int(input("Enter one number: "))
        n2 = int(input("Enter one number: "))
        print(div(n1, n2))
    else:
        print("invaild option")

calculator()




