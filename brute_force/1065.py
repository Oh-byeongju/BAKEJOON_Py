import sys
input = sys.stdin.readline

def cal(A):
    cnt = 0
    for i in range(1, A + 1):
        number_list = list(map(int, str(i)))
        if i < 100:
            cnt += 1
        elif number_list[0] - number_list[1] == number_list[1] - number_list[2]:
            cnt += 1
    return cnt

A = int(input())
print(cal(A))