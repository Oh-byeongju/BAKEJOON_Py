import sys
input = sys.stdin.readline

M = int(input())
board = []
cnt = 0

for i in range(M):
    A, B = map(int, input().split())
    board.append([A, B])

cnt += board[0][1]
i = 1

while i < M:
    cnt += 1
    if cnt%(board[i][0]+board[i][1]) >= board[i][1]:
        i += 1

print(cnt+1)

