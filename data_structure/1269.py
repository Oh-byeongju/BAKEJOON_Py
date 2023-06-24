import sys
input = sys.stdin.readline

A, B = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

result = set(A_list) ^ set(B_list)

print(len(result))