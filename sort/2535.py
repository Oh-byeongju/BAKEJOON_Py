import sys
input = sys.stdin.readline

N = int(input())
N_lists = []

for i in range(N):
    N_list = list(map(int, input().split()))
    N_lists.append(N_list)

N_lists = sorted(N_lists, key = lambda x : -x[2])

for i in range(2, len(N_lists)):
    if N_lists[0][0] == N_lists[1][0] == N_lists[i][0]:
        continue
    else:
        print(*N_lists[0][:2])
        print(*N_lists[1][:2])
        print(*N_lists[i][:2])
        break
