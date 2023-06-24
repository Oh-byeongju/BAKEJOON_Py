import sys
input = sys.stdin.readline

Nums = []
temp = 0

for i in range(1, 46):
    for j in range(i):
        Nums.append(i)

A, B = map(int, input().split())

for i in range(B-A+1):
    temp += Nums[A-1+i]

print(temp)