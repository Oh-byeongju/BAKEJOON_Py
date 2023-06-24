import sys
input = sys.stdin.readline

Max_num = 246913
Nums = [False] * Max_num
Nums[2] = True

for i in range(3, Max_num, 2):
    Nums[i] = True

for i in range(3, Max_num, 2):
    if Nums[i]:
        for j in range(2 * i, Max_num, i):
            Nums[j] = False

while (True):
    N = int(input())
    cnt = 0

    if N == 0:
        exit()

    for i in range(N+1, (N*2)+1):
        if Nums[i]:
            cnt += 1

    print(cnt)