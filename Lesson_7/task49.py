orbits = [tuple(map(int, input().split())) for i in range(int(input('qnt: ')))]

def func(Li):
    dict = {i[0] * i[1]: i for i in Li if i[0] != i[1]} 
    return max(dict.items())[1]

print(func(orbits))
