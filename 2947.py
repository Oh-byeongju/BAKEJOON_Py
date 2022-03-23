import sys
input = sys.stdin.readline

number_list = list(map(int, input().split()))
ans = [1,2,3,4,5]
temp = 0

while number_list != ans:
    for i in range(4):
        if number_list[i] > number_list[i+1]:
            temp = number_list[i]
            number_list[i] = number_list[i+1]
            number_list[i+1] = temp
            print(*number_list)

