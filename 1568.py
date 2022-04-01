import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
temp = 1

while N > 0:
    if N < temp:
        temp = 1
    N -= temp
    temp += 1
    cnt += 1

print(cnt)