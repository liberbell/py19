def nested_hello_fn():

    def hello():
        print("Hello Cathy!")

    hello()

print(nested_hello_fn())