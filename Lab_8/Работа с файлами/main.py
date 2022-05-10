# Task_6

import random as r

f = open('lines.txt', encoding='utf8')
text = f.readlines()
if text:
    print(r.choice(text))

# Task_7

check = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
         "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
         "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
         "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
         "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
         "б": "b", "ю": "ju", "ё": "jo"}

f = open("cyrillic.txt", encoding="utf8")
e = open("transliteration.txt", 'w')
text = f.read()
for i in text:
    if i.lower() in check and i.isupper():
        e.write(str(check[i.lower()])[0].upper() + str(check[i.lower()])[1:len(check[i.lower()]):1])
    elif i in check:
        e.write(check[i])
    else:
        e.write(i)

#Task_8


def reverse():
    f = open("input.dat", 'rb')
    d = f.read()
    e = open('output.dat', 'wb')
    e.write(d[::-1])

reverse()




#Task_9
import numpy as np


a = []
b = []
c = []
f = open("input.txt", encoding='utf8')
l = list(f.read())
l.count()
for i in l:
    if int(i) > 0:
        a.

with open('input.txt', 'r') as f:
    temp = f.read().split()
    print(temp)

metka1 = []
metka2 = []
metka3 = []

temp_i = [int(i) for i in temp]
for i in temp_i:
    if i > 0:
        metka1.append(i)
    elif i < 0:
        metka2.append(i)
    else:
        metka3.append(i)

with open('output.txt', 'w') as o:
    print(len(temp_i), file=o)
    print('1', len(metka1), '-1', len(metka2), '0', len(metka3), file=o)



#Task_10

f = open("linux.bmp", 'rb')
data = list(bytes(f.read()))
data_neg = []
for i, e in enumerate(data):
    if i < 54:
        data_neg.append(e)
    else:
        data_neg.append(255 - e)
o = open("new_linux_negativ.bmp", 'wb')
o.write(bytes(data_neg))













