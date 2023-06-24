import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
cnt = 0
A = 0
B = N-1

number_list = list(map(int, input().split()))
number_list.sort()

while A < B:
    if number_list[A] + number_list[B] == M:
        cnt += 1
        A += 1
        B -= 1
    elif number_list[A] + number_list[B] < M:
        A += 1
    else:
        B -= 1

print(cnt)