counter = {}
for i in input().split():
    counter[i] = counter.get(i, 0) + 1 #Каждое новое слово - ключ, которому
    # соответствует число появлений этого слова в тексте
    print(counter[i] - 1, end=' ')





s = {}

n = int(input())

for i in range(n):

    first, second = input().split()

    s[first] = second

    s[second] = first

print("Input word from dictionary:")

print(s[input()])

#print(d)





d = {}

for i in range(int(input())):
    last_name,number = input().split()
    d[last_name] = d.get(last_name, 0) + int(number)
for candidate, votes in sorted(d.items()):
    print(candidate, votes)


d = {}
a = {}
for i in range(int(input())) :
    file,w,r,x = input().split()
    a = (int(w), int(r), int(x))
    d[file] = a
for j in range(int(input())):
    f,o = input().split()
    if(d.get(f,0)[int(o)] == 1):
        print("Ok")
    else:
        print("Access denied")




actions = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

files = {}
for i in range(int(input())):
    file, *a= input().split()
    # "*" обозначает, что "a" принимает произвольное количество аргументов
    files[file] = set(a)

for i in range(int(input())):
    a, file = input().split()
    if actions[a] in files[file]:
        print('OK')
    else:
        print('Access denied')





d = {}
for i in range(int(input())):
    for word in input().split():
        d[word] = d.get(word, 0) + 1

sorted_input = sorted(d.items(), key = lambda item: item[1])
print(sorted_input)
