import sys

def hello(name):
    print("Hello", name)
    hello(name)

# hello("Ron")

# print(sys.getrecursionlimit())

def increment(num):
    print(num, end = " ")

    increment(num + 1)

    return
