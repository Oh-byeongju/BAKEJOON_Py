import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
result = 0
N_list = sorted(N_list)

for i in range(N):
    if N_list[i] - result >= 2:
        print(result+1)
        exit()
    else:
        result = N_list[i]

if result == max(N_list):
    print(result+1)
else:
    print(result)