# Day 13: Working with CSV & JSON
# CSV module: reading and writing

import csv

fields = []
rows = []

with open("university_recode.csv", "r") as csvFile:
    csvReader = csv.reader(csvFile)

    fields = next(csvReader)
    for row in csvReader:
        rows.append(row)

    # print("total length of row: ", len(row) )
    # print(list(fields))
    # for row in rows[:10]:
    #     print(row)


# fields = ["Name", "Dept.", "Year", "CGPA"]
# row = [
#     ["Mostak", "CSE", "2025", "3.56"],
#     ["Shahariyar", "CSE", "2025", "3.50"],
#     ["Rahin", "CSE", "2025", "3.70"]
# ]
# fileName = "university_recode.csv"

# with open(fileName, "w") as csvFile:
#     csvWrite = csv.writer(csvFile)
#     csvWrite.writerow(fields)
#     csvWrite.writerows(row)
        



# JSON module: loads(), dumps(), load(), dump()

# loads take data or write data in memory, load take data or write in file, is same way for convert data dumps and dump

import json
# json data
x =  '{ "name":"John", "age":30, "city":"New York"}'
load_data = json.loads(x)
# print(load_data)
# a Python object (dict):
x_py = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
json_data = json.dumps(x_py)
# print(x_py)

with open("mtcars.json", "r") as jsonData:
    load_data_file = json.load(jsonData)
    # print(load_data_file)


# Practice: CSV data analyzer, JSON config manager, data converter