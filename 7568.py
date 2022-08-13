import sys
input = sys.stdin.readline

N = int(input())
info_list = []

for i in range(N):
    A, B = map(int, input().split())
    info_list.append((A, B))

for i in info_list:
    cnt = 1
    for j in info_list:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt, end=' ')
