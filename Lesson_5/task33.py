import random
n = int(input("введите количество оценок"))
array = [random.randint(1, 5) for i in range(n)]
print(array)
minn = min(array)
maxn = max(array)
for i in range(n):
    if array[i] == maxn: 
        array[i] = minn
print(array)
num = [minn if i == maxn else i for i in array]
print(num)
