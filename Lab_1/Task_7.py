f=int(input())
if 10000>f>999:
    d =f %10
    c =f //10%10
    b =f //100%10
    a =f //100
    
    if a > b :
        a, b = b, a 
    if b > c :
        b, c = c, b 
    if c > d :
        c, d = d, c 
    if a > b :
        a, b = b, a 
    if b > c :
        b, c = c, b 
    if a > b :
        a, b = b, a 
    if a == 0 and b :
        a, b = b, a 
    elif a == 0 and c :
        a, c = c, a
    elif a == 0 and d :
        a, d = d, a
    print(d + 10 * (c + 10 * (b + 10 * a)))
