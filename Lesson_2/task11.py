n = int(input('Введите число '))
a = 0
b = 1
f = 2
while n >= b:
    if n == b:
        print(f)
        break
    a, b = b, a+b
    f += 1
else:
    print(-1)


# count = 2
# fibo_n = int(input('Input Fibonacci number: '))
# a = 0
# b = 1


# while fibo_n >= b:
#     if fibo_n == b:
#         print(count)
#         break
#     a , b = b, a + b
#     count += 1
# else:
#     print(-1)