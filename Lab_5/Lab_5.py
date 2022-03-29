def triangle(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if(a + b >= c and a + c >= b and b + c >= a):
        print("It's triangle")
    else:
        print("It isn't triangle")

a, b, c = input().split()
triangle(a, b, c)



import math

def distance(x1, y1, x2, y2):
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

x1,y1 = input().split()
x2,y2 = input().split()

print(distance(x1, y1, x2, y2))





def number_to_words(n):
    a = {1: 'один', 2: 'два', 3: 'три', 4 : 'четыре',
         5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
         9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
         16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    b = {10 : 'десять', 20 : 'двадцать', 30 : 'тридцать', 40 : 'сорок',
    50 : 'пятьдесят', 60 : 'шестьдесят', 70 : 'семьдесят',
    80 : 'восемьдесят', 90 : 'девяносто'}
    if(int(n) < 20):
        return a.get(n, 0)
    else:
        return b.get(n // 10 * 10, 0) + " " + a.get(n % 10, 0)

print(number_to_words())   




def power(a, n):
    b = a
    for i in range(abs(n)-1):
        a*=b
    if n > 0:
        return a
    else:
        return 1 / a

print(power(2, -1))





def palindrome(a):
    if(str(a).lower().replace(' ', '') == str(a)[::-1].lower().replace(' ', '')):
        return("Палидром")
    else:
        return("Не палиндром")

print(palindrome('А роза упала на лапу Азора'))




a = set()

def print_without_duplicates(message):
    if message not in a:
        a.add(message)
        print(message)
    else:
        pass

print_without_duplicates('Hello there')
print_without_duplicates('Hello there')
print_without_duplicates('Hello there')
print_without_duplicates('Hello there')
print_without_duplicates('Как дела?')
print_without_duplicates('Как дела?')
print_without_duplicates('Как дела?')
print_without_duplicates('Как дела?')
print_without_duplicates('Hello there')





people = {}

def add_friends(name_of_person, list_of_friends):
    a = people.get(name_of_person, None)
    if a:
        people[name_of_person] = a + list_of_friends
    else:
        people[name_of_person] = list_of_friends

def are_friends(name_1, name_2):
    if name_2 in people[name_1]:
        return True
    return False

def print_friends(name):
    for i in sorted(people[name]):
        print(i, end=' ')

add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))
print_friends("Алла")




def mirror(arr):
    arr += arr[::-1]

arr = [1, 2, 3]
mirror(arr)
print(*arr)




def from_string_to_list(string, container):
    container += list(string.replace(" ", ""))

a = [1, 2, 3]
from_string_to_list("4 5 6 7", a)
print(a)





def transpose(matrix):
    trans_matrix = matrix.copy()
    matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(trans_matrix)):
        for j in range(len(trans_matrix[0])):
            matrix[j][i] = trans_matrix[i][j]
    return matrix

matr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for line in matr:
    print(*line)
print()
matr = transpose(matr)
for line in matr:
    print(*line)





def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        

matr = [[1, 2], [4, 5]]
for line in matr:
    print(*line)
print()

transpose(matr)
for line in matr:
    print(*line)   #Работет только с 2х2









def matrix(n = 1, m = 0, a = 0):
    if m != 0:
        matr = [[a for i in range(n)] for i in range(m)]
    else:
        matr = [[a for i in range(n)] for i in range(n)]
    return matr


rows = matrix()
for i in rows:
    print(*i)
print()
rows = matrix(2)
for i in rows:
    print(*i)
print()
rows = matrix(2, 3)
for i in rows:
    print(*i)
print()
rows = matrix(2, 3, 7)
for i in rows:
    print(*i)














def power(a, n):
  if n == 0:
      return 1
  return a*power(a, n-1)






def recursive_len(a):
    if not a:
        return 0
    return 1 + recursive_len(a[1::])

print(recursive_len([1, 2, 3]))










def linear(some_list):
    if some_list == []:
        return some_list
    if isinstance(some_list[0], list):           # проверка не является ли нулевой элемент списком
        return linear(some_list[0] + linear(some_list[1::]))
    return  some_list[:1:] + linear(some_list[1::])

print(linear([[1, 2], [3, 4]]))
