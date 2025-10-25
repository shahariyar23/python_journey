# Day 11: File Handling
# Opening/closing files (open(), close(), with statement)
# f  = open(r"test.py")
# for i in f:
#     print(i)
# f.close()

# with open("test.py") as f:
#     print(f.read())









# Reading: read(), readline(), readlines()

# with open("test.py") as f:
    # print(f.read())
    # print(f.readline())
    # print(f.readlines()) # it's return as a list object






# Writing: write(), writelines()
# with open("text.txt", "a") as f:
#     f.write("this is text file")

# with open("text.txt", "r") as f:
#     print(f.read())


# with open("text.txt", "w") as f: # write overrite the hole file
#     f.write("Modify this text file")

# with open("text.txt", "r") as f:
#     print(f.read())

# f = open("text.txt", "a")
# f.writelines(["add new line...", "add one more line"])

# f.close()

# f= open("text.txt", "r")
# print(f.read())







# Practice: Note-taking app, file copy program, log file reader

import shutil
def writeNote(note, url):
    with open(url, "a") as f:
        f.writelines(note + "\n")

def readNote(url):
    with open(url, "r") as f:
        print(f.read())

def showLog(url):
    with open(url, "r") as f:
        for line in f:
            yield line.strip()

def copyNoteToAnother(src, des):
    shutil.copyfile(src, des)


if __name__ == "__main__":
    while True:
        print("--------------Welcome to our note taking app--------------")
        print("1. Add Note")
        print("2. Read Note")
        print("3. Show you activity")
        print("4. Copy note to another file. First give source file then give destination file path or name: ")
        print("5. Exit")

        option =  input("Enter your option: ")
        if option == "1":
            url = input("Enter your file name or file path: ")
            note = input("Write your note: ")
            writeNote(note, url)
        elif option == "2":
            url = input("Which note you read enter the file name or file path")
            readNote(url)
        elif option == "3":
            url = input("Enter which file activity you show: ")
            log = showLog(url)
            # print(log)
            for l in log:
                print(l)
        elif option == "4":
            src = input("Enter your source file name or path: ")
            des = input("Enter your destination file name or path: ")
            copyNoteToAnother(src, des)
        elif option == "5":
            break
        else:
            print("You enter wrong option please enter correct option")
    



