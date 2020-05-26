def geterate_even_numbers(limit):
    for i in range(0, limit, 2):
        yield i

g = geterate_even_numbers(7)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# l = list(g)
# print(l)

def generate_squares(limit):
    for i in range(0, limit):
        yield i ** 2

gen = generate_squares(10)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# square_list = list(generate_squares(10))
# print(square_list)

def generate_powers_of_two():
    num = 0
    while True:
        num = num + 1
        yield 2 ** num

gen2 = generate_powers_of_two()
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))