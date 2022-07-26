import sys
input = sys.stdin.readline

M, N = map(int, input().split())

Max_num = 1000001
Nums = [False] * Max_num
Nums[2] = True

for i in range(3, Max_num, 2):
    Nums[i] = True

for i in range(3, N, 2):
    if Nums[i]:
        temp_num = i * i
        if temp_num >= Max_num:
            break
        for j in range(i*2, N, temp_num + i):
            Nums[i] = False
        i = i//2

for num in Nums:
    if num:
        print('dsds')