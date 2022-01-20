import sys
input = sys.stdin.readline

A, B = map(int, input().split())

result = abs(A-B)*2//B

print(result)