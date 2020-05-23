import sys

def hello(name):
    print("Hello", name)
    hello(name)

# hello("Ron")

# print(sys.getrecursionlimit())

sys.setrecursionlimit(100)

def increment(num):
    print(num, end = " ")

    increment(num + 1)

    return

# increment(1)

def decrement(num):
    while num > 0:
        print(num)
        num = num - 1

# decrement(50)

def decrement2(num):
    if num == 0:
        return

    print(num)
    decrement2(num - 1)

decrement2(50)