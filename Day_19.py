# Day 19: Modules & Packages
# Importing modules (import, from...import)
import math 
import math as m
from math import sqrt
print(math.sqrt(8))
print(sqrt(8))
print(m.pi)



# Creating your own modules
from utility import add, welcome
print(add(5,9))
print(welcome("Mostak Shahariyar"))


# name == "main"
# Package structure
import math_utility
import string_utility
print(math_utility(5,5))
print(string_utility("mostak"))
