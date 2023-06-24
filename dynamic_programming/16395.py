import sys
input = sys.stdin.readline

N, K = map(int, input().split())
odd_list = []
even_list = []

if N == 1:
    odd_list = [1]
elif N == 2:
    even_list = [1, 1]
else:
    even_list = [1, 1]

    for i in range(3, N + 1):
        for j in range(i):
            if i % 2 == 1:
                if j == 0 or j == i - 1:
                    odd_list.append(1)
                    if j == i - 1:
                        even_list.clear()
                else:
                    odd_list.append(even_list[j - 1] + even_list[j])
            else:
                if j == 0 or j == i - 1:
                    even_list.append(1)
                    if j == i - 1:
                        odd_list.clear()
                else:
                    even_list.append(odd_list[j - 1] + odd_list[j])

if N % 2 == 1:
    print(odd_list[K - 1])
else:
    print(even_list[K - 1])
