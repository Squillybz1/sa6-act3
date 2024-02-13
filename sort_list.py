
list_1 = ['hello', 'my', 'name', 'is', 'Henryetta']
list_1_sorted = sorted(list_1, key=lambda item: (len(item), item[1]))
print(list_1_sorted)
