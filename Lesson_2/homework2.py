# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
sum = int(input('Введите сумму загаданных чисел:'))
mul = int(input('Введите произведение загаданных чисел:'))
x = 1
for i in range(1000):
    if x*x - sum*x + mul == 0:
        break
    else:
        x += 1
if x == 1001:
    print('Ошибся ты, Петя, не можем найти числа с такими суммой и произведением')
else:
    y = sum-x
    print(x, y)
