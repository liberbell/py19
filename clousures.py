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

greet_fn = greet_by_name("sam")
greet_fn()