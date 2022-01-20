from itertools import permutations
import math

M, N = map(int, input().split())
person = [list(map(int, input().split())) for i in range(3)]
result = float('inf')
# 무슨 수랑 비교해도 무조건 큰 수 나옴
yummi = [M, N]

def cal(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

for i in permutations(person):
    temp = 0
    present = yummi
    for p in i:
        next = p
        temp += cal(present, next)
        present = p

    result = min(result, temp)

print(int(result))