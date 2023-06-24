import sys
input = sys.stdin.readline

M = int(input())
N_set = {0}

for i in range(M):
    temp = input().strip().split()

    if len(temp) == 1:
        if temp[0] == 'all':
            N_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        else:
            N_set = {0}
    else:
        Op, Num = temp[0], temp[1]
        Num = int(Num)

        if Op == 'add':
            N_set.add(Num)
        elif Op == 'remove':
            N_set.discard(Num)
        elif Op == 'check':
            if Num in N_set:
                print('1')
            else:
                print('0')
        elif Op == 'toggle':
            if Num in N_set:
                N_set.discard(Num)
            else:
                N_set.add(Num)
