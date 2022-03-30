import sys
input = sys.stdin.readline

A = str(input().rstrip())
op = str(input().rstrip())
B = str(input().rstrip())

if op == '*':
    print(A + B[1:])
else:
    A = int(A)
    B = int(B)
    print(A+B)
