def astarisk_highlight(func):
    def highlight():
        print("*" * 50)

        func()

        print("*" * 50)

    return highlight

def plus_highlight(func):
    def highlight():
        print("+" * 50)

        func()

        print("+" * 50)
    
    return highlight

@astarisk_highlight
def print_message_one():
    print("Yoohoo, Decorators are cool!")

print_message_one()