import sys
input = sys.stdin.readline

M, N = map(int, input().split())

Max_num = 1000001
Nums = [False] * Max_num
Nums[2] = True

for i in range(3, Max_num, 2):
    Nums[i] = True

for i in range(3, Max_num, 2):
    if Nums[i]:
        for j in range(2 * i, Max_num, i):
            Nums[j] = False

for i in range(M, N+1):
    if Nums[i]:
        print(i)

