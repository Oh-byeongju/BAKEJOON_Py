import sys
input = sys.stdin.readline

dp = [0] * 11
A, B = map(int, input().split())

dp[0] = A

for i in range(1, B+1):
    if i % 1 == 0:
        dp[i] = max(dp[i], int(dp[i-1]*1.05))

    if i >= 3:
        dp[i] = max(dp[i], int(dp[i-3]*1.2))

    if i >= 5:
        dp[i] = max(dp[i], int(dp[i-5]*1.35))

print(dp[B])