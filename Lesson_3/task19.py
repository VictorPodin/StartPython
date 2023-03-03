listik = [1, 2, 3, 4, 5]

k = int(input('Input number: '))

for i in range(k):
    listik.insert(0, listik.pop(-1))

print(listik)