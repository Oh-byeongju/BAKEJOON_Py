import sys
input = sys.stdin.readline

M = int(input())
num_list = list(map(int, input().split()))
cnt = 0

for i in range(M):
    if num_list[i] != i+1:
        cnt += 1

print(cnt)