import sys
input = sys.stdin.readline

A, D, K = map(int, input().split())
Numbers = []
Numbers.append(A)
temp = 0

for i in range(2000002):
    A = A + D
    Numbers.append(A)

for i in range(len(Numbers)):
    if Numbers[i] == K:
        temp = i + 1

if temp == 0:
    print('X')
else:
    print(temp)