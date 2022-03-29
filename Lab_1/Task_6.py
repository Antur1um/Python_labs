l=-1 #max
m = 10 #min
a = int(input())
b = a
if 1000 > a > 99:
    while a > 0:
        if a % 10 > l:
            l = a % 10
        if a % 10 < m:
            m = a % 10
        a = a // 10    
    while b > 0:
        if (l + m) / 2==b % 10:
            print("It is nice number")
            break
        b = b // 10
    if b <= 0:    
        print("It's regular number")    