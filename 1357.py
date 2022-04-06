import sys
input = sys.stdin.readline

def Rev(A):
    A = int(A[::-1])
    return A

A, B = map(str, input().split())
result = Rev(str(Rev(A) + Rev(B)))

print(result)