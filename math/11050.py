import sys
input = sys.stdin.readline

M, N = map(int, input().split())
C = M - N

A_fac = 1
for i in range(1, M+1, 1):
    A_fac = A_fac * i

B_fac = 1
for i in range(1, N+1, 1):
    B_fac = B_fac * i

C_fac = 1
for i in range(1, C+1, 1):
    C_fac = C_fac * i

print(A_fac//(B_fac * C_fac))