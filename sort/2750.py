import sys
input = sys.stdin.readline

N = int(input())
num_list = []

for i in range(N):
    temp = int(input())
    num_list.append(temp)

num_list.sort()

for i in range(N):
    print(num_list[i])