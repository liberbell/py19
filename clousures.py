def nested_hello_fn():

    def hello():
        print("Hello Cathy!")

    hello()

print(nested_hello_fn())

hello_fn = nested_hello_fn()
print(hello_fn)