import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    # 상 우상 우 우하 하 좌하 좌 좌상
    # 8방향 탐색을 위해
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    board[x][y] = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < B and 0 <= ny < A and board[nx][ny] == 1:
            dfs(nx, ny)

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        exit()
    board = []
    cnt = 0
    for _ in range(B):
        board.append(list(map(int, input().split())))
    for i in range(B):
        for j in range(A):
            if board[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)