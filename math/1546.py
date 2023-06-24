import sys
input = sys.stdin.readline

M = int(input())
score_list = list(map(int, input().split()))

result = 0
max_value = max(score_list)

for i in range(M):
    temp = score_list[i]/max_value * 100
    result = result + temp

print(result/M)