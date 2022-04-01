import sys
input = sys.stdin.readline

N = int(input())
N_list = []
value = 5

for i in range(N):
    temp = int(input())
    N_list.append(temp)

for i in range(N):
    cnt = 5
    for j in range(N_list[i], N_list[i]+5):
        if j in N_list:
            cnt -= 1
            value = min(cnt, value)

print(value)
