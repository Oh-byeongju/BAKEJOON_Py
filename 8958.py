import sys
input = sys.stdin.readline

M = int(input())

for i in range(M):
    board = list(input())
    sum = 0
    temp = 1
    for j in board:
        if j == 'O':
            sum += temp
            temp += 1
        else:
            temp = 1
    print(sum)

