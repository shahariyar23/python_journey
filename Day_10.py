# # Day 10: List Comprehensions & Generators
# # List comprehensions syntax

# # system is: newlist = [expression for element in iterative if condition == true]
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # newlist = [x for x in fruits if "a" in x]
# # newlist = [x if x != "banana" else "orange" for x in fruits]
# newlist = [x for x in fruits] #copy list 
# # print(newlist)





# # Dict and set comprehensions
# # {key_expression: value_expression for element in iterable if condition}

# key = ["Name", "Age" , "City"]
# value = ["Mostak Shahariyar", 22, "Uttara"]
# d = dict([(k,v) for k,v in zip(key, value)])
# f = dict([(idx, x )for idx, x in enumerate(fruits)])
# # print(f)





# # Generator expressions
# # it nothing but a function just a short version of function like: (expressionn for element in iterable if condition) (x for in x in fruits)

# from functools import reduce
# # sum of number
# totalSum = (reduce(lambda x, y : x + y, range(1, 6))) # it create a object 
# # print((x for x in range(1, 5))) # when i print it. Gives a object address when use next then it give us one ans at a time 

# num = (x for x in range(1,5))
# for i in num:
    # print(i) #here price all the number one by one






# Practice: Filter even numbers, flatten nested lists, create custom generators

def filterEvenNum():
    return filter(lambda x: x % 2 == 0, range(1, 11))

# print(dict([(idx, x) for idx, x in enumerate(filterEvenNum())])) #we can print as a dictonary 



# print(list(filterEvenNum())) #we can print as a list 

n = filterEvenNum()

for i in n:
    # print(i) #also print as a element by element
    pass





# neste list
listOne = [[1,2,3],[4,5,6],[7,8,9]]
listTwo = [1,[2,[3,[4,[5,[6,[7,[8,[9]]]]]]]]] # it a complex

# lets conver it in flatten list

# flat = []

# for i in listOne:
#     for x in i:
#         flat.append(x)

# user list comprehension
# flat = [x for i in listOne for x in i]

# user generator expression
# flat = (x for i in listOne for x in i)
# print(list(flat))
#  all are same this jus different method


# now list two here it littel bit complex inside list have list agian list inside have list 
# 1. Firts def a function then using loop we access the first list
# 2. Check the next elemet is list or not if list then go through the same function if not retun or using yield 

def flattenList(lst): #create custom generators
    for i in lst:
        if isinstance(i, list): #here isinstance check i is list or not here we can use type also like if type(i) == "list"
            yield from flattenList(i)
        else:
            yield i

# print(list(flattenList(listTwo)))

# create custom generators

def gen(n):
    for i in range(n):
        yield i

for i in gen(10):
    print(i)