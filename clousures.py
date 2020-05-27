def nested_hello_fn():

    def hello():
        print("Hello Cathy!")

    hello()

# print(nested_hello_fn())

hello_fn = nested_hello_fn()
# print(hello_fn())
# hello_fn()

def gread_hello_by_name(name):
    def hello():
        print("Hello!", name)

    hello()

    return hello

gread_hello_fn = gread_hello_by_name("sam")

print(gread_hello_fn) 