list_nums = [0, -1, 5, 2, 3]
print(sum([list_nums[i]>list_nums[i-1]for i in range(1, len(list_nums))]))



# дз
# # n = [int(i) for i in input().split()]
# n = list(map(int, input().split()))
# print(n)