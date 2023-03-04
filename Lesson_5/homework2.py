# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 
A = int(input("Введите A: "))
B = int(input("Введите Б: "))
#res = 1
def rec_sum(A, B):
    if A < 1 or B < 1:
        if A == 0:
            return B
        else:
            return A
    if A < B:
        return rec_sum(A - 1, B + 1)
    else:
        return rec_sum(A + 1, B - 1)
print(rec_sum(A,B))