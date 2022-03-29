import math

def factorials(n):
    for i in range(n + 1):
        yield math.factorial(i)

n = factorials(7)
for i in range(8):
    print(next(n), end = " ")


import math

def factorials(n):
    for i in range(n+1):
        yield math.factorial(i)


n = list(factorials(7))
print(n)
