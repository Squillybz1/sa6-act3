number_1 = [1, 26, 76, 97, 10, 23]
number_2 = [23, 65, 76, 26, 28]
number_3 = number_2 + number_1
intersect = list(filter(lambda x: x in number_2, number_1))
print(intersect)