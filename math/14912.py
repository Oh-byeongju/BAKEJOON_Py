import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0

for i in range(1, N+1):
    cnt += str(i).count(str(M))

print(cnt)