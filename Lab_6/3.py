num = [i + 1 for i in range(9, 99)]
l = sum(map(lambda x: x ** 2, filter(lambda n: n % 9 == 0, num)))
print(num)
print(l)


