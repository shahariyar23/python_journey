# Day 5: Loops - Part 2
# Nested loops (loops inside loops)
print("---------------------nasted loops-----------------------------")
# for x in range(0,2):
#     print(x)
#     for y in range(1,5):
#         print(y)
# i=1
# j=1
# while i < 6:
#     print(i) 
#     while j < i:
#         print("*")
#         j+=1
#     i+=1



# Pattern printing
print("---------------------patternn print-----------------------------")
for x in range(1,6):
    print(x*"*")

for x in range(6,0,-1):
    print(x*"x")

row = 6
for x in range(1, row):
    space = (" " * (row - x))
    star = ("*" * (2 * x - 1 ))
    print(space + star)
e = 0
for x in range(row, 0, -1):
    space = (" " * (e))
    star = ("*" * (2 * x - 1) )
    print( space + star )
    e+=1

print("---------------------loops control-----------------------------")
# Loop control techniques
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
print("Loop finished.")

for i in range(5):
    if i == 2:
        continue  # Skip printing when i is 2
    print(i)

for i in range(3):
    if i == 1:
        pass  # Do nothing when i is 1
    else:
        print(i)

# Practice: Pyramid patterns, prime number checker, Fibonacci series

def pyramidPatterns():
    for i in range(1,6):
        space =" " * (6-i)
        star ="*" * (2 * i -1)
        print(space + star)

# pyramidPatterns()

def primeNumberCheck():
    n = int(input("Enter one number to check it prime or not: "))
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} is not prime number.")
                break
        else:
            print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")
# primeNumberCheck()


def fibonacciSerias():
    n = int(input("enter the number how many need fibonacci searias: "))
    a, b = 0, 1
    for i in range(n):
        # print(a,end=" ") if i use end the show in same line if i dont use end it print is multiple line
        print(a, end=" ")
        a ,b = b, a + b
fibonacciSerias()
