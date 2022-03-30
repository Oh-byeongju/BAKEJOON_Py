import sys
input = sys.stdin.readline

#최대 공약수 구하는법
def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


N = int(input())
N_list = list(map(int, input().split()))
A = N_list[0]

for i in range(N-1):
    temp = gcd(A, N_list[i + 1])
    if temp == 1:
        print(A, '/', N_list[i+1], sep='')
    else:
        print(A // temp, '/', N_list[i+1] // temp, sep='')


