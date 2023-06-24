import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = []
answer = [0 for _ in range(N)]
grade = []

for i in range(N):
    temp_array = sorted(list(map(int, input().split())))
    array.append(temp_array)

for i in range(M):
    temp_array = [j[i] for j in array]
    max_value = max(temp_array)
    for k in range(N):
        if temp_array[k] == max_value:
            answer[k] += 1

max_value = max(answer)

for i in range(N):
    if answer[i] == max_value:
        grade.append(i+1)

print(*grade)


