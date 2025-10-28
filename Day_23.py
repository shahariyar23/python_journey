# Day 23: Advanced Data Structures
# Stack implementation

# class Stack:
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return not bool(self.items)
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         if self.isEmpty():
#             raise IndexError("Stack is empty")
#         return self.items.pop()
#     def peek(self):
#         if self.isEmpty():
#            raise IndexError("Stack is empty")
#         return self.items
#     def reverse(self):
#         if self.isEmpty():
#             raise IndexError("Stack is empty")
#         return self.items[::-1]

# s = Stack()
# s.push(10)
# s.push(20)
# s.push(40)
# s.push(50)
# s.push(60)
# s.push(30) # 30 is at the top
# print(f"Peek: {s.peek()}")  # Output: 30
# print(f"Pop: {s.pop()}")
# print(f"Peek: {s.peek()}")    
# print(f"Pop: {s.pop()}") 
# print(f"Peek: {s.peek()}")   
# print(f"reverse: {s.reverse()}")   
# print(f"Is Empty: {s.isEmpty()}") # Output: False


# Queue implementation
# using list
# class Queue:
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return len(self.items) == 0
#     def enqueue(self, item):
#         self.items.append(item)
#     def dequeue(self):
#         if self.isEmpty():
#             raise IndexError("Queue is empty")
#         return self.items.pop(0)
#     def size(self):
#         return len(self.items)
#     def display(self):
#         return self.items

# using built in function
# from collections import deque
# class Queue:
#     def __init__(self):
#         self.items = deque()
#     def isEmpty(self):
#         return len(self.items) == 0
#     def enqueue(self, item):
#         self.items.append(item)
#     def dequeue(self):
#         if self.isEmpty():
#             raise IndexError("Queue is empty")
#         return self.items.popleft()
#     def size(self):
#         return len(self.items)
#     def display(self):
#         return self.items

# q  = Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)
# print(f"Dequeue: {q.dequeue()}")
# print(f"Dequeue: {q.dequeue()}")
# print(f"Size: {q.size()}")
# print(f"All items: {q.display()}")

# Linked list basics

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
        

# Practice: Build stack, queue, and simple linked list from scratch