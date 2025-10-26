def add(a,b):
    return a + b

def welcome(name):
    print(f"Welcome {name} to visit our site")


if __name__ == "__main__":
    print("Utility module is running directly.")
else:
    print("Utility module is imported.")