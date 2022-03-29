def check_password(func):
    def get_args(n):
        while input() != "12345":
            print('error')
        func(n)
    return get_args

@check_password
def square_fibonacci(n):
    n1, n2 = 0, 1
    for i in range(n):
        n1, n2 = n2, n1 + n2
        print(n1 ** 2)

square_fibonacci(7)
