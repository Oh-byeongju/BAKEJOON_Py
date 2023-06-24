import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
stone = [0] * 100

Blue = 0
Red = 0
Green = 0

for _ in range(M):
    A, B = map(str, input().split())
    A = int(A)
    if B == 'R':
        for i in range(A, 100):
            stone[i] += 1
    else:
        for j in range(0, A - 1):
            stone[j] += 1

for i in range(100):
    if stone[i] % 3 == 0:
        Blue += 1

    elif stone[i] % 3 == 1:
        Red += 1

    else:
        Green += 1

print(format(N * (Blue / 100), ".2f"))
print(format(N * (Red / 100), ".2f"))
print(format(N * (Green / 100), ".2f"))