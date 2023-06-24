import sys
input = sys.stdin.readline

N, X = map(int, input().split())
N_list = list(map(int, input().split()))
N_length = len(N_list)
max_sum = 0
cnt = 1

if max(N_list) == 0:
    print('SAD')
    exit(0)
else:
    window_sum = sum([N_list[i] for i in range(X)])
    max_sum = window_sum

    for i in range(N_length-X):
        window_sum = window_sum - N_list[i] + N_list[i+X]

        if window_sum == max_sum:
            cnt += 1
        elif window_sum > max_sum:
            cnt = 1
            max_sum = window_sum

print(max_sum)
print(cnt)
