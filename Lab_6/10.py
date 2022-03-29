def same_by(characteristic, objects):
    return all(characteristic(i) for i in objects)

l = [1, 2, 32, 64, 5, 66, 7, 12,  8, 1, 5, 7, 2, 3]
if same_by(lambda x: x % 2, l):
    print('same')
else:
    print('different')
