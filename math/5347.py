import sys
input = sys.stdin.readline

T = int(input())
temp = 0

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

for i in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))
