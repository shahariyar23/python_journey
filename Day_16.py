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


x = Student("Mostak Shahariyar", 22, "CSE")
x.displayInfo()
t = Teacher("Shahariyar", 30, "CSE")
t.displayInfo()


# ● Practice: Animal hierarchy (Animal → Dog, Cat), Vehicle system
