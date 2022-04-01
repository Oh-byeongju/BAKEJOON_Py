import sys
input = sys.stdin.readline

while(True):
    M = str(input().rstrip())
    N_list = []

    if M == '0':
        exit()
    for i in range(len(M)):
        N_list.append(M[i])

    if len(M) == 1:
        print('yes')
    elif len(M) == 2:
        if N_list[0] == N_list[1]:
            print('yes')
        else:
            print('no')
    elif len(M) == 3:
        if N_list[0] == N_list[2]:
            print('yes')
        else:
            print('no')
    elif len(M) == 4:
        if N_list[0] == N_list[3] and N_list[1] == N_list[2]:
            print('yes')
        elif N_list[0] == N_list[3] == N_list[1] == N_list[2]:
            print('yes')
        else:
            print('no')
    else:
        if N_list[0] == N_list[4] and N_list[1] == N_list[3]:
            print('yes')
        elif N_list[0] == N_list[4] == N_list[1] == N_list[3]:
            print('yes')
        else:
            print('no')

