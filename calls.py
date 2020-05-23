def factorial(number):
    if number < 0:
        print("Sorry, factorial does not exist for negative numbers")
        return

    if number == 0:
        return 1

    return number * factorial(number - 1)

factorial(3)