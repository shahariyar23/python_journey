# ###########Day 4: Loops - Part 1######################
# -----------------------For loops, range() function--------------------
color = ["red", "green", "white", "black"]
# for x in color:
#     print(x)
# for x in color[3]:
#     print(x)
# # range(start, stop, steps)
# for s in range(3):
#     print(s) # 0,1,2
# for s in range(2,5):
#     print(s) # 2,3,4
# for s in range(2,10, 3):
#     print(s) # 2,5,8

# -----------------While loops---------------
# i = len(color)
# j = 0
# while j < i:
#     print(color[j])
#     j+=1
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   elif i==5:
#     break
#   print(i)

# ------------------------Break and continue----------------------


# Practice: Multiplication tables, sum of n numbers, factorial calculator

def MultiplicaitonTable():
    print("Which number of multiplication table ")
    n1 = int(input())
    for x in range(1,11):
        print(f"{x} x {n1} = {x*n1}")

MultiplicaitonTable()

def sumOfNumber():
    print("How many number you need to sum: ")
    n1 = int(input())
    totalSum = 0
    for x in range(1, n1+1):
        print(f"{x} number: ")
        sn = int(input())
        totalSum +=sn
        print(f"anter adding {sn} your sum is: {totalSum}")

    print(f"Total sum: {totalSum}")

sumOfNumber()

def factorialCalculator():
    print("entrt one number to calculat factorial: ")
    n = int(input())
    
    factorial = 1
    if n<0:
        print("negtaive number have no factorial")
        return
    elif n == 1:
        print(f"1 factorial is 1")
        return
    for x in range(1, n+1):
        factorial*=x
    print(f"{n} factorial is {factorial}")

factorialCalculator()