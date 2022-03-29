num = [1, 2, 3, 4, 5, 6, 7, 8, 1,5,7,2,3]
l = list(filter(lambda n: n < 5, num))
print(l)


num = [1, 2, 3, 4, 5, 2, 3]
l = [i for i in num if i < 5]
print(l)
