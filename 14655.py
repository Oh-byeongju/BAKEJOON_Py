import sys
input = sys.stdin.readline

N = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
result = 0

for i in range(N):
    if 0 < first[i]:
        result += first[i]
    else:
        result += abs(first[i])

    if 0 < second[i]:
        result += second[i]
    else:
        result += abs(second[i])

print(result)