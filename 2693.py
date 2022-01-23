import sys
input = sys.stdin.readline

T = int(input())
num = []
temp = 0

for i in range(T):
    Numbers = list(map(int, input().split()))
    for j in range(3):
        temp = max(Numbers)
        Numbers.remove(temp)
    num.append(temp)

for i in num:
    print(i)