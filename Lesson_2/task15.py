n = int(input('введите количество арбузов'))
maxw = 0
minw = 100
result = 0
for i in range(n):
    w = int(input('введите вес'))
    if w > maxw:
        maxw = w
    if w < minw:
        minw = w
print(minw, maxw)
