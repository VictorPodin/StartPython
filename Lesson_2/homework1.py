# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0 -> 2
coins = int(input('Сколько монеток на столе?'))
side_a = side_b = 0
for i in range(coins):
    side = int(input('введите монеты. Гербом - 1, Решкой - 0: '))
    if side == 1:
        side_a += 1
    elif side == 0:
        side_b += 1
    else:
        print('есть ошибка ввода, дальнейший результат будет некорректен')
        break
if(side_a < side_b):
    print('необходимо перевернуть всего', side_a, 'монет')
else:
    print('необходимо перевернуть всего', side_b, 'монет')