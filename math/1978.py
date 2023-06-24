import sys
input = sys.stdin.readline

cnt = 0
N = int(input())
Nums = list(map(int, input().split()))

for i in range(N):
    temp_Num = Nums[i]
    if temp_Num == 1:
        continue
    for j in range(2, temp_Num+1):
        if temp_Num == j:
            cnt += 1
        if temp_Num % j == 0:
            break

print(cnt)


