import sys
input = sys.stdin.readline

M = int(input())
cnt = 0

for i in range(M):
    board = list(map(int, input().split()))
    sum_score = sum(board) - board[0]
    avg_score = sum_score / board[0]
    A = len(board)-1
    cnt = 0
    for j in range(A):
        if board[j+1] > avg_score:
            cnt += 1
    result = cnt/board[0]*100
    print("%0.3f%%" % result)