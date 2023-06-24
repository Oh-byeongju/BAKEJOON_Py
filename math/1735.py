import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C, D = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

N_lcm = lcm(B, D)   # B,D 최소공배수

A = A * N_lcm // B
B = B * N_lcm // B
C = C * N_lcm // D
D = D * N_lcm // D

result_A = A+C      # 새로운 값
result_B = B        # 새로운 값

N_gcd = 0
N_gcd = gcd(result_A, result_B)     # 새로운 값 최대 공약수

if N_gcd == 0:
    print(result_A, result_B)
else:
    print(result_A//N_gcd, result_B//N_gcd)

