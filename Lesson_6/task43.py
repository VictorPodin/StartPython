# Дан список чисел. Посчитайте,
# сколько в нем пар элементов,
# равных друг другу.

# Считается, что любые два элемента,
# равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел.
# Все числа списка находятся на разных строках.
#sa = set(input().lower().split())
list1 = [1, 2, 3, 4, 2, 3, 4, 3, 5, 6, 5, 3, 3, 3]
# list2 = list(set(list1))
# count = 0
# print(list2)
# for i in range(len(list2)):
#    count+= list1.count(list2[i])//2
# print(count)

#
# dict_list = {}.fromkeys(list1, 0)
# print(dict_list)
# for i in list1:
#     dict_list[i] +=1

# print(sum([i // 2 for i in dict_list.values() if not i % 2]))

#
from time import time
from random import choices 

li = choices(range(3000), k=2000)
sum = 0
start = time()
for i in li:
    a = li.count(i)
    if a > 1:
        if a % 2 != 0:
            sum += (a - 1) / 2
            #li.pop(i)
        else:
            sum += a / 2
print(f'i = {a / 2}, sum = {-(-sum // 4)}')


#li = choices(range(3000), k=2000)

print(time() - start)