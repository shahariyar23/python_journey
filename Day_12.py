# Day 12: Exception Handling
# Try-except blocks
# mulitple except
# raise exception
class InValidInput(Exception):
    pass

# try:
#     n = input("Enter one number: ")
#     if not type(n) is int:
#         raise InValidInput("Must be input in number")
#     print("You entered:", n)
# except ValueError:
#     print("Input must be an integer")
# except InValidInput as e:
#     print("Custom Error:", e)
# finally:
    # print("Try-except finished")


# Practice: Safe calculator, file reader with error handling, input validator

def safeCalculator():
    try:
        print("---------Safe Calculator---------")
        option = input("Enter operation(+, -, *, /): ").strip()
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if option == "+":
            return a + b
        elif option == "-":
            return a - b
        elif option == "*":
            return a * b
        elif option == "/":
            if b == 0:
                raise ZeroDivisionError("Second number can not be zero")
            return a / b
        else:
            raise InValidInput("Wrong option you choose")
    except ZeroDivisionError as e:
        print(e)
    except ValueError:
        print(ValueError)
    except InValidInput as e:
        print(e)

def fileReaderWithErorHandeling():
    try:
        path = input("Enter the file name of file path: ")
        with open(path, "r") as f:
            print(f.read())
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)

def invalidInput():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise InValidInput("Age can not be nagetive!!")
        print(age)
    except InValidInput as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    while True:
        print("1. For calculation")
        print("2. For Read file")
        print("3. For check valid input")
        print("4. For Exit")

        op = input("Enter one operation: ")
        if op == "1":
            print(safeCalculator())
        elif op == "2":
            fileReaderWithErorHandeling()
        elif op == "3":
            invalidInput()
        elif op == "4":
            break
        else:
            print("You enter invalid input")
