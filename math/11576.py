import sys
input = sys.stdin.readline

A, B = map(int, input().split())
M = int(input())
value = 0
result = []
number_list = list(map(int, input().split()))
number_list.reverse()

# 10진수 구하기
for i in range(M):
    value += number_list[i]*(A**i)

while value > 0:
    result.append(value % B)
    value = value // B
result.reverse()

for i in range(len(result)):
    print(result[i], end=' ')


