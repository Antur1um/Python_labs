# Task_1
a = input()
print(a[2])
print(a[-2])
print(a[0:5:1])
print(a[0:-2:1])
print(a[0::2])
print(a[1::2])
print(a[-1::-1])
print(a[-1::-2])
print(len(a))


# Task_2
a = input()
s1 = a[:len(a) // 2]
s2 = a[len(a) // 2:]
print(s2 + s1)


# Task_3
a = input()
f = a[0:a.find('h'):]
s = a[a.rfind('h'):a.find('h'):- 1]
t = a[a.rfind('h')::]
print(f + s + t)


#Task_4
a = input()
f = a.find('f')
s = a.rfind('f')
if f != s and f:
    print(f, s, end=' ')
else:
    print('')


#Task_6
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] * a[i - 1] > 0:
        print(a[i - 1], a[i])
        break



a = [int(i) for i in input().split()]
for i in range(0, len(a) - 1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
print(a)


a = [int(i) for i in input().split()]
for i in range(0, len(a), 1):
    if a[i] not in a[i + 1::] and a[i] not in a[:i:]:
        print(a[i], end=' ')




x = []
y = []
for i in range(8):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

check = True
for i in range(8):
    for j in range(i + 1, 8):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False

if correct:
    print('No')
else:
    print('Yes')








def check(a):
    if max(a) > 8:
        return False
    else:
        for i in range(len(a)):
            if a[i] in a[i + 1::] or a[i] in a[:i-1:]:
                return False
        return True


x = []
y = []
for i in range(8):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

b = True
if check(x) and check(y):
    for i in range(8):
        for j in range(i + 1, 8):
            if abs(x[i] - x[j]) == abs(y[i] - y[j]):
                b = False

if b:
    print("No")
else:
    print("Yes")
