a = int(input())
b = int(input())
simvol = input()
print(simvol * b)
for i in range(a - 2):
    print(simvol, ' ' * (b - 2), simvol, sep='')
print(simvol * b)