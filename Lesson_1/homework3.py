# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
ticket = int(input('Введите номер билета: '))
sum_right = ticket//100000 % 10 + ticket//10000 % 10 + ticket//1000 % 10
sum_left = ticket//100 % 10 + ticket//10 % 10 + ticket % 10
if sum_left==sum_right:
    print('Номер билета счастливый!!!')
else:
    print('номер не счастливый')
