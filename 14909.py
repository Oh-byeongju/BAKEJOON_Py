import sys
input = sys.stdin.readline

Numbers = list(map(int, input().split()))
cnt = 0

for i in range(len(Numbers)):
    if Numbers[i] > 0:
       cnt += 1

print(cnt)