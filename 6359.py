import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    A = int(input())
    test_board = [0] * (A+1)
    for j in range(A):
        k = j + 1
        temp = k
        while(k <= A):
            test_board[k] += 1
            k = k + temp
    cnt = 0
    for l in range(len(test_board)):
        if test_board[l] % 2 == 1:
            cnt += 1
    print(cnt)
