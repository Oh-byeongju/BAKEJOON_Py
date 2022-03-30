import sys
input = sys.stdin.readline

M = int(input())
T_list = list(input())
A_cnt = 0
B_cnt = 0

for i in range(M):
    if T_list[i] == 'A':
        A_cnt += 1
    else:
        B_cnt += 1

if A_cnt > B_cnt:
    print('A')
elif A_cnt < B_cnt:
    print('B')
else:
    print('Tie')