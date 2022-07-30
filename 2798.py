import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number_list = list(map(int, input().split()))
result_list = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if number_list[i] + number_list[j] + number_list[k] <= M:
                result_list.append(number_list[i] + number_list[j] + number_list[k])

print(max(result_list))
