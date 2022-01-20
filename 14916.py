import sys
input = sys.stdin.readline

N = int(input())
div_num = N % 5
cnt = 0

if N == 1 or N == 3:
    print(-1)
    exit()

if div_num % 2 == 0:
    print(N//5 + div_num//2)
    exit()
else:
    print((N//5)-1 + (div_num+5)//2)
    exit()
