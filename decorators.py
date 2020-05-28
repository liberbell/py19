import random

def print_message():
    print("Yoohoo! Decorators are so cool.")

# print_message()

def highlight():
    annotaitions = ["-", "+", "*", "^", ":"]
    annotate = random.choice(annotaitions)

    print(annotate * 40)
    print_message()
    print(annotate * 40)

highlight()