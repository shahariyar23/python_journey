# Day 18: Magic Methods
# str, repr
# len, getitem
# Operator overloading (add, sub, etc.)
# Magic Method	        Purpose	                Example
# __init__	    Initialize object	        obj = MyClass()
# __str__	    String representation       (for user)	print(obj)
# __repr__	    String representation       (for developer)	repr(obj)
# __len__	    Object length	            len(obj)
# __getitem__	Index access	            obj[i]
# __add__	    Addition operator +	        obj1 + obj2
# __sub__	    Subtraction -	            obj1 - obj2
import math

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age}"
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
p = Person("Mostak", 22)
# print(str(p))
# print(repr(p))

class MyList:
    def __init__(self, data):
        self.data =data
    def __len__(self):
        return len(self.data)
    def __getitem__(self, index):
        return self.data[index]
    
l = MyList([10,20,30,40,50])
# print(len(l))
# print(l[1])

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return Point(self.a + other.a, self.b + other.b)
    def __sub__(self, other):
        return Point(self.a - other.a, self.b - other.b)
    def __repr__(self):
        return f"Point {self.a, self.b}"
p1 = Point(4, 5)
p2 = Point(6, 8)

# print(p1 + p2)
# print(p1 - p2)



# Practice: Custom Vector class, Fraction class with operations
class Vector:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
    def __repr__(self):
        return f"Vectior ({self.x}, {self.y})"
    
v1 = Vector(10, 20)
v2 = Vector(1, 2)

print(v1 + v2)
print(v1 - v2)
print(len(v1))


class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.simplefied()
    def simplefied(self):
        g = math.gcd(self.x, self.y)
        self.x //=g
        self.y //=g
    def __add__(self, other):
        newX = self.x * other.y +  self.y * other.x
        newY = self.y * other.y
        return Fraction(newX, newY)
    def __sub__(self, other):
        newX = self.x * other.y -  self.y * other.x
        newY = self.y * other.y
        return Fraction(newX, newY)
    def __str__(self):
        return f"Fraction ({self.x}/{self.y})"
    
f1 = Fraction(6,8)
f2 = Fraction(7,9)

print(f1 + f2)
print(f1 - f2)