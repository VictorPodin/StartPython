# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input('введите количество долек по горизонтали: '))
m = int(input('введите количество долек по вертикали: '))
k = int(input('Сколько хотите попробовать отломить долек на один разлом?: '))
if k%n==0 or k%m==0:
    print('получится', k , 'и', m*n-k ,'долек на двух кусках шоколадки')
else:
    print('не получится')