import sys
input = sys.stdin.readline

N = int(input())

def recur(cnt):     # 3 = 0,, 9 = 1 27 = 3  81 = 9

    print('*' * N)
    print('* *' * (N // 3))
    print('*' * N)

    if cnt < N // 9:
        print('*' * (N // 9) + ' ' * (N // 9) + '*' * (N // 9))
        print('* *' * (N // 9) + ' ' * (N // 3) + '* *' * (N // 9))
        print('*' * (N // 9) + ' ' * (N // 9) + '*' * (N // 9))

        recur(cnt + N // 3)


recur(N//9)

