from math import sqrt as sqrt
x = [2, 1, 1, 1, -1, 1]
y = [1, 1, 2, -1, 2, 0]
print(sorted(zip(x, y), key= lambda x: (sqrt(x[0] ** 2 + x[1] ** 2), x[0], x[1] )))
