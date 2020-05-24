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

def geterate_squares(limit):
    for i in range(0, limit, 2):
        yield i ** 2