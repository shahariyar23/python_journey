# Day 7: Tuples, Sets & Dictionaries
# Tuples: immutable sequences
t1 = ("Mosak", "Shahariyar", "Mostain", "Rahin")
# t1[1] = "Mostak" it does not allow in tupe. because it immutable

# if you conver it list then you change
# (x,y,*z) = t1 # first 2 is print then rest of the element are print in z part
(x, *y, z) = t1 # firs element print in x and last element y and rest of the is y 
# print(x,y,z)



# Sets: unique elements, set operations( after create we can not change but delete and add || here we can not use index or key it show random element and when we pop this time it remdomly remove element)

s1 = {"Apple", "Reamle", "Xiaomi", "Techno"}
s2 = {"Mac", "iPhone", "iMac", "Mackbook"}
s3 = s1.union(s2) # also use update
s1.add("Nothing") # also use update
s1.discard("Apple") # use also remove but this element is not present then rise an error
s3.clear() #clear the set
del s3 # del all the set
s4 = s1.copy()
s4.pop() # rendomly remove
print(s1)


# Dictionaries: key-value pairs, dict methods

d1 = {
    "name": "Mostak Shahariyar",
    "age": 22,
    "deparment": "CSE"
}

for i, j in d1.items():
    print(i, j)

print(d1.get("name"))
print(d1.items())
print(d1.keys())
d1.pop("age")
d1["age"] = 22


# Practice: Student database, remove duplicates, word counter

studentDB = {
    22203208: ("Mostak", "CSE", 22),
    22203207: ("Mostain", "CSE", 28),
    22203206: ("Babla", "CSE", 22),
    22203205: ("Nur", "CSE", 22),
}

for i, j in studentDB.items():
    print(i, j)

studentName = ["mostak","mostain", "rahin", "rahin","mostak"]
print(set((studentName)))

text = "this is test to check the work count is correct or not"
words = text.split()
word = {}

for i in words:
    if i in word:
        word[i] += 1
    else:
        word[i] = 1

print(word)