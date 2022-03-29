
num = [1, 2, 32, 64, 5, 66, 7, 12,  8, 1, 5, 7, 2, 3]
l = list(map(lambda x: x / 2, filter(lambda n: n > 17, num)))
print(l)


num = [1, 2, 32, 64, 5, 66, 7, 12,  8, 1, 5, 7, 2, 3]
l = [i / 2 for i in num if i > 17]
print(l)
