import sys
input = sys.stdin.readline

board = []

for i in range(9):
    temp = int(input())
    board.append(temp)

num = max(board)
print(max(board))
print((board.index(num))+1)