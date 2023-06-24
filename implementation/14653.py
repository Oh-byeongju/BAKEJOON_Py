import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())
eng_list = []

for i in range(N):
    eng_list.append(chr(65+i))

check = [0] * 26
check[0] = 1
data = [[0,'']]

for i in range(K):
    A, B = input().split()
    data.append([int(A), B])

if data[Q][0] == 0:
    print(-1)
    exit()

for i in range(1, K+1):
    if data[Q][0] <= data[i][0]:
        check[eng_list.index(data[i][1])] = 1

for i in range(N):
    if not check[i]:
        print(eng_list[i], end=' ')