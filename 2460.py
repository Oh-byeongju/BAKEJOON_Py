import sys
input = sys.stdin.readline

max_value = 0
temp_value = 0

for i in range(10):
    A, B = map(int, input().split())
    temp_value = temp_value - A
    temp_value = temp_value + B
    max_value = max(temp_value, max_value)

print(max_value)