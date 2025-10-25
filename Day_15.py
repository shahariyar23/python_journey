# Day 15: OOP - Part 2
# Class variables
# Instance vs class methods
class School:
    school_name = "ABC"
    def __init__(self, name,age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    @classmethod
    def changeSchoolName(self, schoolName):
        self.school_name = schoolName
    def displayInfo(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Grade: ", self.grade)

School.changeSchoolName("IUBAT")
s1 = School("Mostak", 22, "Male")
# print(s1.displayInfo())

# Static methods
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    @staticmethod
    def isAdult(age):
        return age >= 18
    
p = Person("mostak", "Male")
# print(Person.isAdult(19))
# Practice: Employee management system with different methods

class Employee:
    companyName = "XYZ"
    totalNumberEmployee = 0
    def __init__(self, name, dept, age):
        self.name = name
        self.dept =dept
        self.age = age
        Employee.totalNumberEmployee += 1
    def displayInfo(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Department: ", self.dept)
    @classmethod
    def changeCompanyName(cls, value):
        cls.changeCompanyName = value
        print("Company name change: ", cls.changeCompanyName)
    @classmethod
    def totalEmployee(cls):
        print("Total employee: ", cls.totalNumberEmployee)
    @staticmethod
    def salary(perHouerMoney, hours):
        return perHouerMoney * hours

Employee.changeCompanyName("Tech pro")   
e = Employee("Mostak", "developer", 22)
e.displayInfo()
e.totalEmployee()
print(f"Salary: {Employee.salary(200,36)}")
    
