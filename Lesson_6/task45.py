# все делители числа 284
# 220 = 1 + 2 + 4 + 71 + 142
# все делители числа 220
# 284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110
# ввод 300
# вывод 220 284
# sum1, sum2 = 0, 0
# for i in range(1, 9999):
#     for k in range(1, i // 2 + 1):
#         if i % k == 0:
#             sum1 += k
#     for j in range(i + 1, 9999):
#         if j == i:
#             continue
#         for k in range(1, j // 2 + 1):
#             if j % k == 0:
#                 sum2 += k
#         if sum1 == j and sum2 == i:
#             print(i, j, sep=' ')
#     sum1, sum2 = 0, 0
li = []
user_in = (int(input("Input a number: ")))

start = time()
def sum_dev(num):
    cou = 1
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            cou += i + num / i
    return cou

for j in range(10, user_in):
    first = sum_dev(j)
    second = sum_dev(first)
    if second == j and first < second:
        print(j, first)

print(time() - start)