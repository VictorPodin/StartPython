# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

n = int(input("Введите количество элементов: "))
array = [randint(1, 5) for i in range(n)]
print(array)
maxi = int(input("Введите максимум диапазона: "))
mini = int(input("Введите минимум диапазона: "))
array_res = [i for i in range(n) if mini <= array[i] <= maxi]
print("Индексы элементов в диапазоне:", array_res)