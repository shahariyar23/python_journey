# Day 2: Operators & String Manipulation

# Arithmetic
x = 2 + 3 # 5 addition +
y = 20 - 10 # 10 suntraction -
z = 5 / 2 # 2.5 (float) division /
m = 12 / 5 # 2 modulus %
e = 4 ** 2 # 8 (pow 4^2) Exponentiation **
f = 5 / 2 # 2 (int) Floor division //

#comparison (give the answer either true or false)
xE = "mostak" == 5 # (answer is false) ==
xNE = "mostak" != 5 # (answer is true) !=
xG = 6 > 5 # (true) >
xL = 7 < 8 # (true) <
xGE = 5 >= 10 # (false) >=
xLE = 5 <= 10  # (True) <=

#  logical (answer either true or flase)
xA = 2 > 3 and 3 < 5 # (false) and
xR = 2 > 3 or 3 < 5 # (true) or
xN = not(2 > 3 and 3 < 5) # (true) not

# assignment operators
eX = 5 # (5) =
eX += 5 # (10) +=
eX -= 5 # (0) -=
eX *= 5 # (25) *=
eX /= 2 # (2.5) /=
eX %= 2 # (2) %=
eX //= 2 # (2) //=
eX **= 2 # (25) **=
x &= 2 # (0) &=
x |= 2 # (7) |=
x ^= 2 # (7) ^= xor opreation 
x >>= 2 # (1) right shipt
x <<= 2 # (20) left shipt


# string idexing and find

xstr = "Mostak Shahariyar"
# index(value, start, end)
# print(xstr.index("o"))
# print(xstr.index("a",12))
# print(xstr.find("a"))
# print(xstr.find("m")) #it return -1 
# print(xstr.index("m")) #it return and exception


# slicing
# print(xstr[2:5]) #b[strat:end] end value is not include
# print(xstr[:6]) # b[start first : 6]
# print(xstr[5:]) # b[5: end]
# print(xstr[-5:-3]) # b[end to count start : show value ]
# print(xstr[-5:]) # b[end to count start : all   ]
# print(xstr[:: -2], "rev") # reverser string [start: stop: steps]

# concatenation
# print("Mostak" + "Shahariyar")
# print("Mostak" + " " + "Shahariyar")

# String methods: upper(), lower(), strip(), split()
# print(xstr.upper())
# print(xstr.lower())
# print(xstr.split(" "))
# print ("mostak shahariyar  ".strip()) #remove the extra space from beginning and ending


# Practice: Temperature converter, string reverser, basic calculator

def temperatureConver():
    choice = input("1. f to c \n 2. c to f")
    if(choice in "1"):
        f = input("Enter tempareture in f: ")
        c = (float(f) - 32) *5/9
        print(f"{f} to {c:.2f}c")

    if(choice in "2"):
        c = input("Enter tempareture in c: ")
        f = (float(c) * 9/5) + 32
        print(f"{c} to {f:.2f}f")

def stringReverser():
    string = input("Enter one string: ")
    print(string[::-1])

def calculator():
    print("1. Add(+)")
    print("2. Sub(-)")
    print("3. Mul(*)")
    print("4. Div(/)")
    choice = input("Which operation u do: ")
    if(choice in "1" or "+"):
        n1 = int(input("enter one number: "))
        n2 = int(input("enter one number: "))
        print(f"{n1} + {n2} = {n1 + n2}")

    if(choice in "2" or "-"):
        n1 = int(input("enter one number: "))
        n2 = int(input("enter one number: "))
        print(f"{n1} - {n2} = {n1 - n2}")

    if(choice in "3" or "*"):
        n1 = int(input("enter one number: "))
        n2 = int(input("enter one number: "))
        print(f"{n1} * {n2} = {n1 * n2}")

    if(choice in "4" or "/"):
        n1 = int(input("enter one number: "))
        n2 = int(input("enter one number: "))
        print(f"{n1} / {n2} = {n1 / n2}")


if __name__ == "__main__":
    print("1. Calculate temperatue ")
    print("2. Reverse String")
    print("3. Calculator")
    choice = input("Enter which operation you do: ")
    if(choice in "1"):
        temperatureConver()
    if(choice in "2"):
        stringReverser()
    if(choice in "3"):
        calculator()


    

