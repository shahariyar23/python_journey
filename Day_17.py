# Day 17: OOP - Polymorphism & Encapsulation
# Polymorphism concept
# Private and protected members (__and __)
# Property decorators (@property)

class Student:
    def __init__(self, name, age):
        self._name = name
        self.__age= age
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, newName):
        self._name = newName

# s = Student("Mostak", 22)
# s.name = "Shahariyar"
# print(s.name)
# print(s._Student__age)





# Practice: Shape area calculator, secure password manager
import math
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius
    def area(self):
        return 2 * math.pi * self._radius
class Ractangel(Shape):
    def __init__(self, weidth, heigh):
        self.weidth =weidth
        self.heigh = heigh
    def area(self):
        return self.weidth * self.heigh

c = Circle(5)
r = Ractangel(6,5) 
# print(c.area())
# print(r.area())

class PasswordManagement:
    def __init__(self, password):
        self.__password = password
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, newPasswrod):
        self.__password = newPasswrod

p = PasswordManagement("mostak0190")
print(p.password)
p.password = "mostak"
print(p.password)