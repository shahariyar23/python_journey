# Day 20: Popular Built-in Modules
# math, random, datetime

import math
import random
from datetime import date, datetime, timedelta
# print(math.pi)
# print(math.floor(2.60))
# print(math.ceil(2.60))
# print(random.choice([1,2,3,4,5,6]))
# print(random.randint(1,6))
# print(random.choice(['red', 'blue', 'green']))  # random item
# print(int(random.random()*10000)) 
# print("today: ", date.today())
# print(datetime.now())
# print(date.today() + timedelta(days=10))

# os, sys modules
import os
# print(os.getcwd())
# print(os.listdir())
# print(os.rename("test.py", "testFile.py"))
# os.rmdir("__pycache__")

import sys

# print(sys.version)       # Python version
# print(sys.platform)      # OS name
# print(sys.argv)          # Command line arguments



# collections (Counter, defaultdict, namedtuple)

from collections import Counter, defaultdict, namedtuple

nums = [1,2,3,4,5,6,1,1,1,1,1]
print(Counter(nums))


d = defaultdict(list) #here we can use list, set, dict, int, also lamda function
d["fruits"].append("apple")
d["fruits"].append("banna")
d["number"].append(1)
d["number"].append(2)
print(d)

l = defaultdict(lambda: "Not avaiable")

l["mostak"]=45
print(l["mostak"])
print(l["mostaka"])


person = namedtuple("Person",["name", "age"])
p = person("Mostak Shahariyar", 22)
print(p)

# Practice: Dice simulator, file organizer, date calculator


def roll_dice():
    return random.randint(1, 6)  
while True:
    input("Press Enter to roll the dice... ")
    print(f"🎲 You rolled: {roll_dice()}")
    
    again = input("Roll again? (y/n): ").lower()
    if again != 'y':
        break

# roll_dice()

import shutil
# here base on the extention go all the file on this extention folder

def organize_file(folder_path):
    for filename in os.listdir(folder_path):
        name, ext = os.path.splitext(filename)
        ext = ext[1:]
        if not ext:
            continue
        folder_name = os.path.join(folder_path, ext.upper()) 
        os.makedirs(folder_name, exist_ok=True)
        shutil.move(
            os.path.join(folder_path, filename),
            os.path.join(folder_name, filename)
        )
    print("File organize successfully")

# organize_file(r"C:\Users\22203\Downloads\stitch_home_page\stitch_home_page")


def date_calculator():
    date1 = datetime(2025, 12, 25)
    date2 = datetime(2025, 11, 25)
    print(f"Different between two date: {date1 - date2}")

    print(f"after 30 date {date1.strftime('%y-%m-%d')} to {(date1 + timedelta(days=30)).strftime('%Y-%m-%d')}")
date_calculator()