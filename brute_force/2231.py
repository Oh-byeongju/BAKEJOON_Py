import sys
input = sys.stdin.readline

N = input()
temp_int = len(N) - 1
int_N = int(N)

if int_N <= 20:
    for_int = 1
else:
    for_int = int_N - 9 * temp_int

for i in range(for_int, int_N):
    temp_num = i
    sum_res = temp_num

    while (temp_num != 0):
        sum_res = sum_res + temp_num % 10
        temp_num = temp_num // 10

    if sum_res == int_N:
        print(i)
        exit()

print(0)