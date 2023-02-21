n = int(input('введите количество дней:'))
count = 0
result = 0
for i in range(n):
    temp = int(input('введите температуру'))
    if temp > 0:
        count += 1
    else:
        if result < count:
            result = count
        count = 0
print(result)
