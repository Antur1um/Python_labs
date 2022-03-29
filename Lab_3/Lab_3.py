print(len(set([int(s) for s in input().split()])))


print(len(set([int(s) for s in input().split()]).intersection(set([int(i) for i in input().split()]))))





a = [int(s) for s in input().split()]
s = set()
for i in range(len(a)):
    if a[i] in s:
        print(a[i], ' Yes')
    else:
        print(a[i], ' No')
        s.add(a[i])



a = set()
for i in range(int(input())):
    a.update(input().split())
print(len(a))
