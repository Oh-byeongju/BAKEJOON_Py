import sys
input = sys.stdin.readline

X, Y = map(int, input().split())

print(X + Y + (min(X, Y)//10))