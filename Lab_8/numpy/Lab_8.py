# Task_1

# Task_a

import numpy as np

a = np.ones((3, 4)) * 3
print(a)

# Task_b
import numpy as np

a = np.random.randint(0, 9, 8).reshape(2, 4)
print(a)

# Task_c

import numpy as np

arr_1 = np.ones((3, 4)) * 3
arr_2 = np.random.randint(0, 9, 8).reshape(2, 4)
print(arr_1)
print()
print(arr_2)
print()
print(np.size(arr_1))
print()
print(np.size(arr_2))

# Task_d
import numpy as np

arr_1 = np.ones((3, 4)) * 3
arr_2 = np.random.randint(0, 9, 8).reshape(2, 4)
arr_3 = np.concatenate((arr_1, arr_2), axis=0)
print(arr_3)

arr_3 = np.concatenate((np.ones((3, 4)) * 3, np.random.randint(0, 9, 8).reshape(2, 4)), axis=0)
print(arr_3)

# Task_e
import numpy as np

a = (1, 8, 6, 5, 8, 3)
arr_3 = np.array(a)
print(arr_3)

# Task_f
import numpy as np

a = (1, 8, 6, 5, 8, 3)
arr_3 = np.array(a)
arr_4 = (arr_3 * 3) + 1
print(arr_4)

# Task_g
import numpy as np

a = (1, 8, 6, 5, 8, 3)
arr_3 = np.array(a)
arr_5 = arr_3.reshape(2, 3)
print(arr_5)

# Task_h
import numpy as np

a = (1, 8, 6, 5, 8, 3)
arr_3 = np.array(a)
arr_5 = arr_3.reshape(2, 3)
print(arr_5)
print()
print(np.amin(arr_5, axis=1))  # наименьшее число в каждой строке

# Task_i
import numpy as np

a = (1, 8, 6, 5, 8, 3)
arr_3 = np.array(a)
arr_5 = arr_3.reshape(2, 3)
print(arr_5)
print(np.average(arr_5))

# Task_j
import numpy as np

arr_6 = np.square(np.arange(11))
print(arr_6)

# Task_k
import numpy as np

arr_6 = np.square(np.arange(11))
print(arr_6)
print()
print(arr_6[::2])

# Task_m
import numpy as np

arr_6 = np.square(np.arange(11))
print(arr_6)
print()
arr_6[::2] = 2
print(arr_6)

# Task_n
import numpy as np

arr_6 = np.square(np.arange(11))
arr_6[::2] = 2
print(arr_6)
print(np.in1d(49, arr_6))

# Task_o
import numpy as np

A = np.random.randint(-5, 5, 10).reshape(5, 2)
print(A)
B = A[A < 0]
print()
print(B)

# Task_2

import numpy as np


def make_field(size):
    board = np.tile(np.array([[1, 0], [0, 1]]), (size // 2, size // 2))
    return board.astype(np.int8)


a = int(input("Input size: "))
b = make_field(a)
print(b)

# Task_3


import numpy as np


def super_sort(rows, cols):
    A = np.random.randint(0, 100, (rows * cols)).reshape(rows, cols)
    B = np.copy(A)
    B[:, 1::2] = np.sort(B[:, 1::2], axis=0)
    B[:, ::2] = np.sort(B[:, 1::2], axis=0)[::-1]
    return (A, B)

print(super_sort(2, 10))

import numpy as np

A = np.random.randint(0, 100, (4 * 5)).reshape(4, 5)
print(A)
print()
B = A

print(C)
print(sorted(B, key=lambda row: row[2]))
print(C)
print()
print(B)

A = np.random.randint(1, 100, (2 * 2)).reshape(2, 2)
print(A)

# Task_4

from PIL import Image
import numpy as np


def bw_convert():
    a = np.asarray(Image.open('xp.jpg'), dtype='uint8')
    print(a)
    b = np.array([0.2989, 0.587, 0.114])
    sums = np.round(np.sum(a * b, axis=2)).astype(np.uint8)
    k = np.repeat(sums, 3).reshape(a.shape)
    Image.fromarray(k).save('res(2).jpg')


bw_convert()

# Task_5

import numpy as np

table = np.genfromtxt("ABBREV.csv", delimiter=";", dtype=None, names=True)
max_kcal_name = table[np.argmax(table['Energ_Kcal'])]['Shrt_Desc']
print('1)', max_kcal_name)
max_sugar_name = table[np.argmax(table['Sugar_Tot_g'])]['Shrt_Desc']
print('2)', max_sugar_name)
max_protein_name = table[np.argmax(table['Protein_g'])]['Shrt_Desc']
print('3)', max_protein_name)
max_vit_c_name = table[np.argmax(table['Vit_C_mg'])]['Shrt_Desc']
print('4)', max_vit_c_name)



















import numpy as np

table = np.genfromtxt('ABBREV.csv', delimiter=';', dtype=None, names=True, encoding="utf8")

print(table)
