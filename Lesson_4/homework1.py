# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

num1 = int(input("Введите кол-во элементов первого набора: "))
num2 = int(input("Введите кол-во элементов второго набора: "))
nums1 = []
nums2 = []
nums = []
for i in range(num1):
    nums1.append(input("введите элемент первого списка: "))
for i in range(num2):
    nums2.append(input("введите элемент второго списка: "))
print(nums1)
print(nums2)
print(sorted(set(nums1 + nums2)))
#n, m = input().split()
#first = [int(i) for i in input().split()]
#second = [int(j) for j in input().split()]
#print(*sorted(set(first).intersection(second)))