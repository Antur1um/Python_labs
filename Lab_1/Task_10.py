def fac(n):
    factorial = 1
    if int(n) > 1:
        for i in range(2, n + 1):
            factorial *= i
    else:
        return "Error"
    return factorial    
 


def calcul(a,x,y):
    if a==" + ":
        return x + y
    elif a==" - ":
        return x - y
    elif a==" * ":
        return x * y
    elif a==" / ":
        if y==0:
            return"Error"
        return x//y
    elif a==" % ":
        return x % y
    elif a=="!":
        if x > 0:
            return fac(x) 
ans = [] 
while True:
    a = int(input())
    b = input()
    if b!="!" and b!="x":
        c = int(input()) 
    if b!="x" and b!= "!":
        ans.append(calcul(b,a,c))
    elif b=="!":
        ans.append(fac(a))
    else:
        ans.append(a)
        print("\n")
        for i in ans:
            if i!= "Error":
                print(i)
        break   