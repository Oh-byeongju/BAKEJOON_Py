import sys
input = sys.stdin.readline

N = int(input())
board = []
result = []

for i in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)


def cal(x, y, N):
    number = board[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if number != board[i][j]:
                cal(x, y, N // 2)
                cal(x, y + N // 2, N // 2)
                cal(x + N // 2, y, N // 2)
                cal(x + N // 2, y + N // 2, N // 2)
                return
    if number == 0:
        result.append(0)
    else:
        result.append(1)

cal(0, 0, N)
print(result.count(0))
print(result.count(1))
