import sys
input = sys.stdin.readline

N, M = map(int, input().split())
key = 0

for _ in range(M):
    A = int(input())
    N_list = list(map(int, input().split()))
    for j in range(A-1):
        if N_list[j] < N_list[j+1]:
            print("No")
            exit()
print("Yes")