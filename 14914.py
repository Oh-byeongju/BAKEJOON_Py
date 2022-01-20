import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = []

for i in range(1, N + 1):
    if (N % i == 0) & (M % i == 0):
        data.append(i)

for i in data:
    print(i, N//i, M//i)

