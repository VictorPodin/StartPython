# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1

N = int(input("Введите N: "))
list = [int(input("Введите элемент массива:")) for i in range(N)]
print(list)
X = int(input("Введите искомое число X: "))
print(list)
count = 0
for i in list:
    if i == X:
        count += 1
print(f"Число {X} встречается в списке {count} раза")