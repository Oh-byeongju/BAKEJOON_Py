import sys
input = sys.stdin.readline

N = int(input())
Days = [0] * 32

for i in range(N):
    A, B = map(int, input().split())
    for j in range(A, B):
        Days[j] += 1

M = int(input())

if max(Days) > M:
    print(0)
else:
    print(1)