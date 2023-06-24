import sys
input = sys.stdin.readline

def check(x, y):
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if visited[nx][ny] == 1:
            return 0
    return 1

def value(cnt):
    global total, answer

    if cnt == 3:
        answer = min(answer, total)
        return

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if check(i, j) == 1:
                for k in range(5):
                    x = i + dx[k]
                    y = j + dy[k]
                    visited[x][y] = True
                    total += board[x][y]
                value(cnt + 1)
                for k in range(5):
                    x = i + dx[k]
                    y = j + dy[k]
                    visited[x][y] = False
                    total -= board[x][y]

N = int(input())
board = []
answer = 9999999
total = 0
# 자신 상 하 좌 우
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
visited = [[False] * N for _ in range(N)]

for i in range(N):
    board.append(list(map(int, input().split())))

value(0)
print(answer)


