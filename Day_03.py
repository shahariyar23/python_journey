# Day 3: Conditional Statements
# if, elif, else statements
if(100> 5):
    print("100 is bigger then 5")
else:
    print("5 is bigger then 100")

n = 80
if n >= 80:
    print("A+")
elif n>75:
    print("A")
elif n>70:
    print("A-")






# Nested conditionals

if (n >= 0 and n <= 100):
    if n > 79 :
        print("A+")
    elif n > 74: 
        print("A")

else:
    print("invalid number")


# Ternary operator

print("A+") if(n > 79) else print("less then A+") if(n >= 0 and n <= 100) else print("invalid number")

# Practice: Grade calculator, leap year checker, largest of 3 numbers


def gradeCalculator():
    mark = int(input("Enter you marks: "))
    if( mark >= 0 and mark <=100):
        if mark > 79:
            print("Your grade is A+")
        elif mark > 75:
            print("Your grade is A")
        elif mark > 69:
            print("Your grade is A-")
        elif mark > 64:
            print("Your grade is B+")
        elif mark > 59:
            print("Your grade is B")
        elif mark > 54:
            print("Your grade is B-")
        elif mark > 49:
            print("Your grade is C+")
        elif mark > 44:
            print("Your grade is C")
        elif mark > 39:
            print("Your grade is D")
        else:
            print("Sorry!!! Your grade is F")
    else: 
        print("invalid marks!!! please enter a valid marks")


def leapYearCheck():
    year = int(input("Enter the year to check it leap year or not: "))
    print(f"{year} is leap year") if year % 400 == 0 else print(f"{year} is leap year") if (year % 4== 0 and year % 100 !=0) else print(f"{year} is not leap year")


def checkNumberLarger():
    print("Enter three number: ")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    print(f"{n1} is larger nunber") if (n1 > n2 and n1 > n3) else print(f"{n2} is larger number") if (n2 > n1 and n2 > n3) else print(f"{n3} is a larger number")

if __name__ == "__main__":
    print("1. grade calculation")
    print("2. Check leap year")
    print("3. Check 3 larger number")

    choice = input()

    if choice in "1":
        gradeCalculator()
    elif choice in "2":
        leapYearCheck()
    elif choice in "3":
        checkNumberLarger()
    else:
        print("Invalid input!!!")
