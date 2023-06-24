import sys
input = sys.stdin.readline

board = []
cnt = 0

for i in range(10):
    temp = int(input())
    div = temp % 42
    board.append(div)

result = list(set(board))
cnt = len(result)

print(cnt)