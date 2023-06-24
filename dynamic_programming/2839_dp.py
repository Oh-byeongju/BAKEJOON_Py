import sys
input = sys.stdin.readline

N = int(input())
Nums = [3, 5]

dp = [float('inf')] * 5001
dp[0] = 0

for i in range(2):
    # Nums[i]가 가는 범위
    for j in range(Nums[i], N + 1):
        # Nums[i]로 N을 나눴을 때 나머지가 없는 범위
        if dp[j - Nums[i]] != float('inf'):
            dp[j] = min(dp[j], dp[j - Nums[i]] + 1)

# 계산된 결과 출력
if dp[N] == float('inf'):
    print(-1)
else:
    print(dp[N])

