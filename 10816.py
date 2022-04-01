import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
res_list = list(map(int, input().split()))

diction = {}

for Number in N_list:
    if Number in diction:
        diction[Number] += 1
    else:
        diction[Number] = 1

for res in res_list:
    result = diction.get(res)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")
