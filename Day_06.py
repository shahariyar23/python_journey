# Day 6: Lists

# List creation, indexing, slicing

# name = [["Mostak", 22], ["Shahariyar", 20], ["Rahin", 21], ["Mostain", 23], ["Rasel", 25]]
# for i in name:
#     print(f"Name: {i[0]} | Age: {i[1]}")
    
#  # index(element, start, end)
# print(name.index(["Rahin", 21]))

# for i in range(len(name)):
#     if name[i][0] == "Rahin":
#         print(f"Rahin index is : {i}")

# # slice
# # list_name[ start : end : step ]
# print(name[2:4:])
    

# # List methods: append(), remove(), pop(), sort(), reverse()

# name.append(["Shown", 21])
# for i in name:
#     print (i)

# name.remove(["Shahariyar", 20])
# # remove(element) only use element
# for i in name:
#     print(i)
# # pop(index number) only use index number

# name.pop(1)

# for i in name: 
#     print(i)

# # after sort by name
# print("after sort by name")
# name.sort(key= lambda x: x[0])

# for i in name:
#     print(i)

# # after sort by age 
# print("after sort by price")
# name.sort( key = lambda x: x[1])
# for i in name:
#     print(i)


# # after reverse
# print("after revers list")
# name.reverse()
# for i in name:
#     print(i)


# # count()
# print(name.count(["Mostak", 22]))


# List operations
# Practice: Todo list app, find max/min in list, list operations
import datetime

def addTask(todoListTask, existenLength):
    task = input("Add you Task: ")
    todoListTask.append([task, datetime.date.today()])
    if existenLength < len(todoListTask):
        print("Task added successfully")
        fetchTask(todoListTask)
        exit
    else:
        print("Some thing is wrong")
        exit


def updateTask(todoListTask):
    fetchTask(todoListTask)
    taskNumber = int(input("Which number of task you updateed: "))
    task = input("Enter the updated task: ")
    todoListTask[taskNumber][taskNumber] = [task, datetime.datetime.today()]

def removeTask( todoListTask, existenLength):
    fetchTask(todoListTask)
    taskNumber = int(input('Which one you can delete: '))
    todoListTask.pop(taskNumber)
    if existenLength > len(todoListTask):
        print("Delete Successfully")
    else:
        print("Some thing is wrong")

def clearTask(todoListTask):
    todoListTask.clear()
    if todoListTask == 0:
        print("All task deleted")
    else:
        print("Some this wrong")

def fetchTask(todoListTask):
    for idTask, i in enumerate(todoListTask, start= 0):
        print(f"{idTask}. Task: {i[0]}   Date: {i[1]}")


def todoList():
    todoListTask = []
    

    while True:
        print("----------------------Todo menu-----------------------------------")
        print("1. Add to task for today")
        print("2. Update your task")
        print("3. Remove task")
        print("4. Deleted all task")
        print("5. Show all your task")
        print("6. Exit")

        chocie = input("Which option you want to go: ")
        if chocie == "1":
            addTask(todoListTask, len(todoListTask))
        elif chocie == "2":
            updateTask(todoListTask)
        elif chocie == "3":
            removeTask(todoListTask, len(todoListTask))
        elif chocie == "4":
            clearTask(todoListTask)
        elif chocie == "5":
            fetchTask(todoListTask)
        elif chocie == "6":
            print("Exiting..")
            break
        else:
            print("Invalid input!!")




if __name__ == "__main__":
    todoList()
