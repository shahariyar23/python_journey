# Day 8: Functions - Part 1
# Function definition and calling
def oneFunction():
    pass

# calling
oneFunction()


# Parameters and arguments
def twoFunction(name):
    print(name)
twoFunction("Mostak")

# Return statements
def threeFunction(x,y):
    return x*y

threeFunction(2,5)

def argFucntion(*x):
    print(x)

argFucntion("mostak", "shahariyar", "shown")

def keywordFunction(**x):
    print(x["f"])

keywordFunction(f="mostak", l="shahariyar")
# Scope (local vs global)
x=200
def scopeGlobal():
    print (x)
    def scopeLoacl():
        x=100 # also her we can use global keyword to global variable use this variable
        print(x)
    scopeLoacl()

scopeGlobal()
# Practice: Create utility functions (isPrime, factorial, palindrome checker)

def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True

def factorial(n):
    if n >= 1:
       return n*factorial(n-1)
    else:
        return 1
    
def palindrom(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
    
def utility():
    n = int(input("Enter a number to check is prime, factorial, and palindrom: "))
    if(isPrime(n)):
        print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")
    print("factorial is: ", factorial(n))
    if palindrom(n):
        print(f"{n} is palindrom number")
    else:
        print(f"{n} is not palindrom number")

utility()
