import sys
input = sys.stdin.readline

T = int(input())
num = []
temp = 0

for i in range(T):
    Numbers = list(map(int, input().split()))
    A = Numbers[0] * 350.34
    B = Numbers[1] * 230.90
    C = Numbers[2] * 190.55
    D = Numbers[3] * 125.30
    E = Numbers[4] * 180.90
    temp = A+B+C+D+E
    num.append(temp)

for i in num:
    print("$%.2f" % i)