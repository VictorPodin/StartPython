# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
A = int(input("Введите A: "))
B = int(input("Введите Б: "))
res = 1
def rec_exponentiation(A, B, res):
    res = res * A
    if B == 1:
        return res
    else:
        return rec_exponentiation (A, B - 1, res)
print(rec_exponentiation(A,B,res))