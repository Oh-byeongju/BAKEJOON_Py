import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
Nums = []

for i in range(M, N+1):
    temp_Num = i
    if temp_Num == 1:
        continue
    for j in range(2, temp_Num+1):
        if temp_Num == j:
            Nums.append(temp_Num)
        if temp_Num % j == 0:
            break

if len(Nums) == 0:
    print(-1)
    exit()

print(sum(Nums))
print(min(Nums))


