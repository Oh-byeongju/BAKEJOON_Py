import sys
input = sys.stdin.readline

def fac(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    result = fac(B) // (fac(A) * fac(B-A))
    print(result)