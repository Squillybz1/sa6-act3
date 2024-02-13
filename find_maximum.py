from functools import reduce
numbers = [1, 24, 3, 48, 5, 6, 47, 8]

print(reduce(lambda x, y: x if x >= y else y, numbers))

