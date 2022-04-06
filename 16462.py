import sys
input = sys.stdin.readline

N = int(input())
N_list = []

for i in range(N):
    Numbers = str(input().rstrip())
    temp_list = []
    for Number in Numbers:
        if Numbers == '100':
            temp_list.append(int(Numbers))
            continue
        elif Number == '0' or Number == '6' or Number == '9':
            temp_list.append(9)
        else:
            temp_list.append(int(Number))
    if len(temp_list) == 2:
        temp = (temp_list[0] * 10) + (temp_list[1] * 1)
    else:
        temp = temp_list[0] * 1
    N_list.append(temp)

result = (sum(N_list)/N)
result = result + 0.5
print(int(result))
