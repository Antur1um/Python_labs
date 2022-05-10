# Task_11

import csv

def print_all():
    with open('shop.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
        expensive = list(reader)
    for i in expensive:
        print(i)
    print()

def add_new():
    print("Input name: ")
    n = input()
    print("Input price for psc: ")
    p = input()
    print("Input number")
    num = input()
    data = [n, p, num]
    f = open('shop.csv', encoding="utf8", mode="r")
    w = csv.writer(f)
    w.writerows(data)

i = 0
while i != 4:
    print("Choose action:", "\n"  "1. Print all", "\n" "2. Add new", "\n"
                                                                     "3. Delete product", "\n" "4. Edit product" "\n",
          "4. Exit ")
    i = input()
    match i:
        case "1":
            print_all()
        case "2":
            print("Input name: ")
            n = input()
            print("Input price for psc: ")
            p = input()
            print("Input number")
            num = input()
            data = [n, p, num]
            f = open('shop.csv', encoding="utf8", mode="r")
            w = csv.writer(f)
            w.writerows(data)

import csv

with open('shop.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    expensive = list(reader)

for i in expensive:
    print(i)

# Task_12
import csv

with open('price.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    expensive = list(reader)

for i in expensive:
    if int(i['old_price']) > int(i['new_price']):
        print(i)

# Task_13
import csv

d = {}
s, cl = input().split()
with open('rez.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for i in list(reader)[1:]:
        info = i[2].split('-')
        name = i[1].split()[3]
        score = int(i[-1])
        if int(s) == int(info[2]) and int(cl) == int(info[3]):
            if str(score) not in d:
                d[str(score)] = []
                d[str(score)].append(name)
            else:
                d[str(score)].append(name)
for i in d:
    d[i].sort(reverse=True)
d = list(d.items())
d.sort(key=lambda i: int(i[0]), reverse=True)
for key, val in d:
    for i in val:
        print(i, key)





























import csv
import re

f = open("rez.csv", encoding="utf8")
r = csv.DictReader(f, delimiter=',', quotechar='"')
data = list(r)
for i in data:
    if (i['user_name'])[2:4:1] == "33":
        print(i['user_name'], i['Score'])

import csv
import re

f = open("rez.csv", encoding="utf8")
r = csv.DictReader(f, delimiter=',', quotechar='"')
data = list(r)
for i in data:
    if re.fullmatch('\*36\*10\*', str(i['user_name'])):
        print(i['user_name'], i['Score'])
