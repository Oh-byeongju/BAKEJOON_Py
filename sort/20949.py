import sys
input = sys.stdin.readline

N = int(input())
M_list = []

for i in range(N):
    A, B = map(int, input().split())
    M_list.append(((A ** 2) + (B ** 2)) ** (1/2) / 77)

for i in range(N):
    temp = M_list.index(max(M_list))
    print(temp+1)
    M_list.insert(temp, 0)
    M_list.remove(max(M_list))
