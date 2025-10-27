# Day 21: Regular Expressions
# re module basics
# Patterns: search(), match(), findall()
import re


txt = "This is a text"
x = re.search("^T.*t$", txt)
if x:
    print("Yes! search is match")
else:
    print("No. match")

print(re.findall("is", txt))
match = re.match("This", txt)
if match:
    print("Yess!! match the pattern")



# Common patterns (email, phone, URL validation)
def validationEmail(email):
    checkEmail = re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)
    if checkEmail:
        return True
    else:
        False

def validationPhone(phone):
    checkPhone = re.match(r"^01[3-9][0-9]{8}$", phone)
    if checkPhone:
        return True
    else:
        False
def validationURL(url):
    checkURL = re.match(r"^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\[w./?%&=-]*)$",url)
    if checkURL:
        return True
    else:
        False

def validationPassword(password):
    checkPassword = re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password)
    if checkPassword:
        return True
    else:
        False

if __name__ == "__main__":
    password = input("Enter you password: ")
    if validationPassword(password):
        print("Your password is strong")
    else:
        print("Your password is week please enter at last 8 password one upper one lower one digit and one spical charter")
    email = input("Enter you email: ")
    if validationEmail(email):
        print("Your email is correct")
    else:
        print("Your mail is not correct")
    phone = input("Enter you phone: ")
    if validationPhone(phone):
        print("You phone number is correct")
    else:
        print("Your number is wrong please at first input 0 then other 10 digit")
    url = input("Enter you url: ")
    if validationURL(url):
        print("Your url is correct")
    else:
        print("Your url is not correct we only accept https and https")

