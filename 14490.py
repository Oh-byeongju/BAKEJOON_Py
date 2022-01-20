import sys
input = sys.stdin.readline

M, N = map(int, input().split(':'))

def div(a, b):
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a
a = div(M,N)

print(M//a,':',N//a,sep='')
