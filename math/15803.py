import sys
input = sys.stdin.readline

A_list = []
B_list = []

for i in range(3):
    A, B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)

if A_list[0] == A_list[1] == A_list[2]:
    print('WHERE IS MY CHICKEN?')
    exit()

if A_list[1] - A_list[0] == 0 or A_list[2] - A_list[1] == 0 or A_list[0] - A_list[2] == 0:
    print('WINNER WINNER CHICKEN DINNER!')
    exit()

if (B_list[1] - B_list[0]) / (A_list[1] - A_list[0]) == (B_list[2] - B_list[1]) / (A_list[2] - A_list[1]):
    print('WHERE IS MY CHICKEN?')
else:
    print('WINNER WINNER CHICKEN DINNER!')
