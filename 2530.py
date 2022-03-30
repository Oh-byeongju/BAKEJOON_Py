import sys
input = sys.stdin.readline

temp = 0

H, M, S = map(int, input().split())
second = int(input())

temp_H = second // 3600
temp = second % 3600

temp_M = temp // 60
temp = temp % 60

temp_S = temp

H = H + temp_H
M = M + temp_M
S = S + temp_S

if S >= 60:
    S = S - 60
    M = M + 1

if M >= 60:
    M = M - 60
    H = H + 1

if H >= 24:
    H = H % 24

print(H, M, S)