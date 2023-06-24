import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    cnt = 0
    A, B = map(int, input().split())
    for j in range(A, B+1):
        temp = str(j)
        cnt += temp.count('0')
    print(cnt)