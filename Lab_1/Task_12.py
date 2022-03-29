n = int(input())
l = 1 # level
y = 0 # number of elements
for i in range(1,n+1) :
    print(i, end=' ')
    y = y + 1
    if y == l :
        print()
        l = l + 1
        y = 0
