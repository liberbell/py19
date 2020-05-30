import random
import math

def print_message():
    print("Yoohoo! Decorators are so cool.")

# print_message()

def highlight():
    annotaitions = ["-", "+", "*", "^", ":"]
    annotate = random.choice(annotaitions)

    print(annotate * 40)
    print_message()
    print(annotate * 40)

# highlight()

def print_another_message():
    print("Did you know? Decolaters use clousures.")

# highlight()

def make_highlighted(func):
    annotaitions = ["-", "+", "*", "^", ":"]
    annotate = random.choice(annotaitions)

    def highlight():
        print(annotate * 40)

        func()

        print(annotate * 40)

    return highlight()

# print_message()
# print_another_message()

# highlight_and_print_message = make_highlighted(print_message)
# highlight_and_print_message()

# highlight_and_print_another_message = make_highlighted(print_another_message)

# @make_highlighted
# def print_a_third_message():
#     print("Now you`ll see how decorators are used")

# @make_highlighted
# def print_any_messages():
#     print("This is an important result that needs to be highlighted!")

def area_circle_fn(radius):
    return math.pi * radius * radius

# def perimeter_circle_fn(radius):
#     return 2 * math.pi * radius

# def diameter_circle_fn(radius):
#     return 2 * radius

# print(area_circle_fn(10))
# print(area_circle_fn(5))
# print(area_circle_fn(-1))

def safe_calculate(func):
    def calculate(r):
        if r <= 0:
            raise ValueError("Radius cannot be negative or zero")

        return func(r)

    return calculate

# area_circle_safe = safe_calculate(area_circle_fn)
# print(area_circle_safe(-1))
# print(area_circle_safe(5))

# perimeter_circle_safe = safe_calculate(perimeter_circle_fn)
# print(perimeter_circle_safe(10))
# print(perimeter_circle_safe(-10))

@safe_calculate
def area_circle_fn(radisu):
    return math.pi * radisu * radisu

@safe_calculate
def perimeter_circle_fn(radisu):
    return 2 * math.pi * radisu

print(perimeter_circle_fn(3))
print(perimeter_circle_fn(-3))

@safe_calculate
def area_rectangle_fn(length, breadth):
    return length * breadth