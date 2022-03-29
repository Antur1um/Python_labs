b = []
mx = -1
mi = 190

c = 0
while True:
    a = input()
    if a != "!":
        if 150 < int(a) < 190:
            b.append(int(a))
    elif a=="!":
        break;
for i in b:
    if i > mx:
        mx = i
    if i < mi:
        mi = i
    c+=1  
print(c)
print(mx)
print(mi)