def factorial(number):
    if number < 0:
        print("Sorry, factorial does not exist for negative numbers")
        return

    if number == 0:
        return 1

    return number * factorial(number - 1)

# print(factorial(10))

def fibonacci(number, fib_series):
    if number < 2:
        return

    l = len(fib_series)

    new_number = fib_series[l - 1] + fib_series[l - 2]
    fib_series.append(new_number)
    fibonacci(number - 1, fib_series)

# series = [0, 1]
# print(fibonacci(10, series))
# print(series)

def fibonacci2(number, fib_series):
    if number < 2:
        return

    l = len(fib_series)

    new_number = fib_series[l - 1] + fib_series[l - 2]
    fib_series.append(new_number)
    print("Series so far ", fib_series)
    fibonacci2(number - 1, fib_series)

series = [0, 1]
print(fibonacci(10, series))
# print(series)