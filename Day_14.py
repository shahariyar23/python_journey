# Day 14: Object-Oriented Programming - Part 1
# Classes and objects

class MyClass:
    name = "Mostak"

n = MyClass()
# print(n.name)

# init constructor
# self keyword
# Instance variables and methods

class MyCar:
    def __init__(self, name, model):
        self.name = name
        self.model = model

bugadi = MyCar("Bugadi", "Bugadi90")
# print(bugadi.name)

# Practice: Create Person, Car, and BankAccount classes

class Car:
    def __init__(self, name, model, year, price, fuel):
        self.name = name
        self.model = model
        self.year = year
        self.price = price
        self.fuel = fuel
    def displayInfo(self):
        print("--------------Car info--------------")
        print("Name: ", self.name)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print("Price: ", self.price)
        print("Fuel: ", self.fuel)
    
class Person:
    def __init__(self, name, age, gender):
        self.name =name
        self.age =age
        self.gender = gender
    def displayInfo(self):
        print("--------------Person info--------------")
        print("Name: ",self.name)    
        print("Age: ",self.age)    
        print("Gender: ",self.gender)

class BankAccount:
    def __init__(self, name, age, gender, accountType):
        self.name = name
        self.age = age
        self.gender = gender
        self.accountType = accountType
    def disPlayInfo(self):
        print("--------------Bank account info--------------")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gende: ", self.gender)
        print("Account type: ", self.accountType)

car1 = Car("Rolls Royle", "vendom", "2021", 2000000, "25L")
car2 = Car("Supra", "gtr", "2021", 200000, "25L")

car1.displayInfo()
car2.displayInfo()

person1 = Person("Mostak Shahariyar", 22, "Male")
person2 = Person("Mostain", 22, "Male")
person3 = Person("Rahin", 22, "Male")

person1.displayInfo()
person2.displayInfo()
person3.displayInfo()

bankAccount1 = BankAccount("Mostak Shahariyar", 20, "Male", "saving")
bankAccount2 = BankAccount("Mostain", 25, "Male", "saving")
bankAccount3 = BankAccount("Rahin", 23, "Male", "Crdit")

bankAccount1.disPlayInfo()
bankAccount2.disPlayInfo()
bankAccount3.disPlayInfo()