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

@make_highlighted
def print_a_third_message():
    print("Now you`ll see how decorators are used")

@make_highlighted
def print_any_messages():
    print("This is an important result that needs to be highlighted!")