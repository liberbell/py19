import random

def nested_hello_fn():

    def hello():
        print("Hello Cathy!")

    hello()

# print(nested_hello_fn())

# hello_fn = nested_hello_fn()6

# print(hello_fn())
# hello_fn()

def gread_hello_by_name(name):
    def hello():
        print("Hello!", name)

    hello()

    return hello

# gread_hello_fn = gread_hello_by_name("sam")
# gread_hello_fn()
# print(gread_hello_fn) 

def greet_by_name(name):
    greeting_msg = "Hi there."

    def greeting():
        print(greeting_msg, name)

    return greeting

# greet_fn = greet_by_name("sam")
# greet_fn()

# del greet_by_name
# greet_by_name("Sam")

def greet_with_personal_message(name, message):
    annotations = ['-', '+', '*', ':', '^']
    annotate = random.choice(annotations)

    def greeting():
        print(annotate * 50)
        print(message, name)
        print(annotate * 50)

    return greeting

greet_tonny_fn = greet_with_personal_message("Tonny", "Hello!")
greet_claudia_fn = greet_with_personal_message("Cludia", "Goody!")
greet_Bob_fn = greet_with_personal_message("Bob", "Howdy?")
# greet_tonny_fn()
# greet_claudia_fn()
# greet_Bob_fn()

def enroll_in_college(college_name):
    student_list = []

    def enroll_student(student_name):
        student_list.append(student_name)
        print("Student", student_name, "has been enrolled in", college_name)
        print("Current status", student_list, end="\n\n")

    return enroll_student