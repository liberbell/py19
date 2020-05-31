def astarisk_highlight(func):
    def highlight():
        print("*" * 50)

        func()

        print("*" * 50)

    return highlight