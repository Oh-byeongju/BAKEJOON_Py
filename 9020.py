import sys
input = sys.stdin.readline

Max_num = 5100
Nums = [False] * Max_num
prime = [2]

for i in range(3, Max_num, 2):
    Nums[i] = True

for i in range(3, Max_num, 2):
    if Nums[i]:
        prime.append(i)
        for j in range(2 * i, Max_num, i):
            Nums[j] = False

T = int(input())

for i in range(T):
    N = int(input())

    A, B = N // 2, N // 2
    while A > 1:
        if A in prime and B in prime:
            print(A, B)
            break
        else:
            A -= 1
            B += 1