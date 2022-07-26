import sys
input = sys.stdin.readline

N = int(input())

def fac(x):
    num = 2

    while num <= x:
        if x % num == 0:
            print(num)
            x = x / num
        else:
            num = num + 1

fac(N)