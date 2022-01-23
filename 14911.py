import sys
input = sys.stdin.readline
from itertools import combinations

nums = sorted(map(int, input().split()))
num = int(input())
cnt = 0
result = []

for i in combinations(nums, 2):
    if sum(i) == num and [i[0], i[1]] not in result:
        result.append([i[0], i[1]])
        cnt += 1

for i in range(cnt):
    print(result[i][0], result[i][1])
print(cnt)