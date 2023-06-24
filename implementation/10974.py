import sys
from itertools import permutations
input = sys.stdin.readline

A = int(input())
arr = []
result = 1

for i in range(A):
    arr.append(i+1)

temp_list = list(permutations(arr, A))

for item in range(1, A+1, 1):
    result *= item

for i in range(result):
    print(*temp_list[i])




