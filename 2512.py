import sys
input = sys.stdin.readline

M = int(input())
N_list = list(map(int, input().split()))
N = int(input())

low = 0
high = max(N_list)
total = 0

if sum(N_list) <= total:
    print(max(N_list))
else:
    while low <= high:
        mid = (low + high) // 2
        total = 0

        for i in N_list:
            if i > mid:
                total += mid
            else:
                total += i

        if total > N:
            high = mid - 1
        else:
            low = mid + 1
    print(high)