
number = '123456789101112'
from functools import reduce

def sum_of_digits(number):
    number_list = []
    for a in number:
        number_list.append(int(a))
    
    sum_of_digits_1 = reduce(lambda x, y: x + y, number_list)

    print(sum_of_digits_1)

sum_of_digits(number)