import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

M, N = map(int, input().split())
M = M - 1
N = N - 1

board = []
safe_x = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
safe_y = set()
is_bomed = False
min_move = 18

#2차원 배열 생성
for i in range(10):
    temp = list(input())
    board.append(temp)

for i in range(10):
    for j in range(10):
        if board[i][j] == 'o':
            safe_x.discard(j)
            # 폭탄 체크용
            is_bomed = True

        if j == 9:
            if is_bomed == False:
                safe_y.add(i)

            # 폭탄 초기화
            is_bomed = False

for x in safe_x:
    for y in safe_y:
        temp_min_move = abs(x - N) + abs(y - M)
        if temp_min_move < min_move:
            min_move = temp_min_move

print(min_move)