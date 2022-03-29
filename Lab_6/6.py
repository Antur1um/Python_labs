def square_fibonacci(n):
    n1, n2 = 0, 1
    for i in range(n):
        n1, n2 = n2, n1 + n2
        yield n1 ** 2

l = list(square_fibonacci(7))
print(l)
