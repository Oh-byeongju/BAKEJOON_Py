import sys
input = sys.stdin.readline

A = int(input())
cnt = 0

res = 1000 - A
div_num = [500, 100, 50, 10, 5, 1]

for i in div_num:
    cnt += res // i
    res %= i
print(cnt)
