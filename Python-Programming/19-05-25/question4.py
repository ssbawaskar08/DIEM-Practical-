even = list(filter(lambda x: x))
even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(1, 101))))
print(even_squares)