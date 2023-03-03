# n = int(input())
# max_number = 0
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)


# Petya

n = int(input())
max_number = -1
while n != 0:
    if max_number < n:
        max_number = n
    n = int(input())
print(max_number)

# https://stepik.org/lesson/482377/step/1?unit=473680

print((lambda s1, s2: s1*s2), num(2, 3))
