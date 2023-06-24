import sys
input = sys.stdin.readline

glass = list(map(str, input().strip()))
result = 10

for i in range(len(glass)-1):
    if glass[i] == glass[i+1]:
        result += 5
    else:
        result += 10
print(result)

