import sys
input = sys.stdin.readline

N = int(input())
lists = list(map(int, input().split()))
cnt = 0
max_cnt = 0
board = [False] * 100001

for i in lists:
    if not board[i]:
        cnt += 1
        board[i] = True
    else:
        cnt -= 1
        board[i] = False
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
