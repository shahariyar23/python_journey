# Day 16: OOP - Inheritance
# ● Single inheritance
# ● Method overriding
# ● super() function
class Person:
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept
    def displayInfo(self):
        print(f"Welcome to our University {self.name}")

    
class Student(Person):
    def __init__(self, name, age, dept):
        Person.__init__(self, name, age, dept)
    def displayInfo(self):
        super().displayInfo()
        print(f"Your seleted as a student {self.name}")


class Teacher(Person):
    def __init__(self, name, age, dept):
        super().__init__(name, age, dept)
    def displayInfo(self):
        super().displayInfo()
        print(f"Your are seleted as a faculty of IUBAT {self.name}")


# x = Student("Mostak Shahariyar", 22, "CSE")
# x.displayInfo()
# t = Teacher("Shahariyar", 30, "CSE")
# t.displayInfo()


# ● Practice: Animal hierarchy (Animal → Dog, Cat), Vehicle system

class Animal:
    def __init__(self, name):
        self.name = name
    def info(self):
        print(f"This animal name is {self.name}")
    def sound(self):
        print("This animal sound is ....")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  
    def info(self):
        print(f"This dog name is {self.name}")
    def sound(self):
        print("This dog sound is woof woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)  
    def info(self):
        print(f"This cat name is {self.name}")
    def sound(self):
        print("This cat sound is Meow Meow!")

d = Dog("dog1")
d.info()
d.sound()

c = Cat("cat1")
c.info()
c.sound()


class Vechicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def showInfo(self):
        print(f"Brand is : {self.brand}")
        print(f"Top speed is : {self.speed} k/m")

class Car(Vechicle):
    def __init__(self, brand, speed, door):
        self.door = door
        super().__init__(brand, speed)
    def showInfo(self):
        super().showInfo()
        print(f"This car have {self.door} door")

class Bike(Vechicle):
    def __init__(self, brand, speed, cc):
        self.cc = cc
        super().__init__(brand, speed)
    def showInfo(self):
        super().showInfo()
        print(f"This Bike have {self.cc} cc")

c = Car("BMW", 400, 4)
c.showInfo()
b = Bike("Kwashaki", 400, 1000)
b.showInfo()