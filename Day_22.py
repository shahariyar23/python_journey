# Day 22: Iterators & Decorators
# Iterator protocol (iter, next)

nums = [1,2,3,4,5]
it = iter(nums)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) # here raise an error stopiteration




# Creating custom iterators



# Decorator basics and syntax

def decorator(func):
    print("Print berfor funtion run")
    func()
    print("After funciton run")

@decorator
def func():
    print("This print from function")



# Practice: Custom range iterator, timing decorator, logging decorator
class myIteration:
    def __init__(self, current, end):
        self.current = current
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

# for i in myIteration(1, 10):
#     print(i)

import time
def time_decorator(func):
    def wraper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} take {end - start:.2f} seconds")
        return result
    return wraper
@time_decorator
def takeTime():
    time.sleep(2)
    print("Finsished ")

takeTime()
