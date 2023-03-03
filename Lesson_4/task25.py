# ang_dict = {"AEIOULNSTRАВЕИНОРСТ": 1, "DGДКЛМПУ": 2,
#             "BCMPБГЁЬЯ": 3, "FHVWYЙЫ": 4, "KЖЗХЦЧ": 5,
#             "JXШЭЮ": 8, "QZФЩЪ": 10}

# word = input()

# print(sum([i[1] for i in ang_dict.items() for j in word if j.upper() in i[0]]))

# text = input().split()
# dict = {}

# for i in text:
#     if i in dict:
#         print(f'{i}_{dict[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     dict[i] = dict.get(i, 0) + 1


chr = input().split()
dict_ch = {}.fromkeys(chr, 0)
print(dict_ch)

for i in chr:
    print(f"{i}_{dict_ch[i]}" if dict_ch[i] else i, end= " ")
    dict_ch[i] += 1