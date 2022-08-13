import sys
input = sys.stdin.readline

M, N = map(int, input().split())
board = []
min_count = float('inf')
count_list = []

for i in range(M):
    temp = list(input().rstrip())
    board.append(temp)

for i in range(M):
    for j in range(N):
        if N-j > 7 and M-i > 7:
            cnt1 = 0
            for k in range(8):
                if k % 2 == 0:
                    check_point = 'B'
                else:
                    check_point = 'W'
                for o in range(8):  # [0][0] ~ [0][7]
                    if o % 2 == 0:
                        if check_point != board[k+i][o+j]:
                            cnt1 += 1
                    if o % 2 == 1:
                        if check_point == board[k+i][o+j]:
                            cnt1 += 1
        count_list.append(cnt1)

        if N-j > 7 and M-i > 7:
            cnt2 = 0
            for k in range(8):
                if k % 2 == 0:
                    check_point = 'W'
                else:
                    check_point = 'B'
                for o in range(8):  # [0][0] ~ [0][7]
                    if o % 2 == 0:
                        if check_point != board[k+i][o+j]:
                            cnt2 += 1
                    if o % 2 == 1:
                        if check_point == board[k+i][o+j]:
                            cnt2 += 1
        count_list.append(cnt2)

print(min(count_list))