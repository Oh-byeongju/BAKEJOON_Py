import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())
G = int(input())
H = int(input())
J = int(input())
K = int(input())

Numbers = [B,C,D,E,F,G,H,J,K]
N_sum = sum(Numbers)
no_num = A - N_sum

print(no_num)
