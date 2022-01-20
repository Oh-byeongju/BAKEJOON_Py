import sys
input = sys.stdin.readline

M, N = map(int, input().split())
board = []
Rownum = []
Colnum = []

for i in range(M):
    temp = list(map(str, input().split()))
    board.append(temp)
    Rowcnt = 0
    for j in temp:
        Rowcnt += j.count('9')
    Rownum.append(Rowcnt)

for i in range(N):
    Colcnt = 0
    for j in range(M):
        Colcnt += board[j][i].count('9')
    Colnum.append(Colcnt)

A = max(Colnum)
B = max(Rownum)
C = max(A, B)

print(sum(Rownum) - C)