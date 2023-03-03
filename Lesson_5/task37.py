# N = input()
# print(N[::-1])

def reorder(number):
    if number == 0:
        return ""
    strochechka = input()
    return reorder(number - 1) + strochechka

N = int(input())
print(reorder(N))