def arithmetic_operation(op):
    def plus(a, b):
        return a + b

    def minus(a, b):
        return a - b

    def mult(a, b):
        return a * b

    def devide(a, b):
        return a // b

    if op == '+':
        return plus
    elif op == '-':
        return minus
    elif op == '*':
        return mult
    elif op == '//':
        return devide


operation = arithmetic_operation('+')
print(operation(3, 4))
