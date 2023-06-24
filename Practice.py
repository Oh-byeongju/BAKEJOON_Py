import sys
input = sys.stdin.readline

A, B = map(int, input().split())

res = A - B
print(abs(res))
