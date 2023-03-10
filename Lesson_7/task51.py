# Напишите функцию same_by(characteristic, objects),
# которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True,
# если это так. Если значение характеристики для
# разных объектов отличается - то False.
# Для пустого набора объектов,
# функция должна возвращать True.
# Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.

values = []

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

# values = [3, 3, 5, 7]

def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) == 1

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')