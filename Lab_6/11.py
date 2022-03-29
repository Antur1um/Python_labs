
def print_operation_table(operation, num_rows = 9, num_columns = 9):
    for j in range(1, num_rows + 1):
        print(*(operation (j, k) for k in range(1, num_columns + 1 )))
# Звездочка нужна для захвата нескольких чисел.

print_operation_table(lambda x, y: x * y)

