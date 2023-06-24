import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    A = A % 10
    if A == 1:
        print('1')
    elif A == 2:
        if B % 4 == 1:
            print('2')
        elif B % 4 == 2:
            print('4')
        elif B % 4 == 3:
            print('8')
        else:
            print('6')
    elif A == 3:
        if B % 4 == 1:
            print('3')
        elif B % 4 == 2:
            print('9')
        elif B % 4 == 3:
            print('7')
        else:
            print('1')
    elif A == 4:
        if B % 2 == 1:
            print('4')
        else:
            print('6')
    elif A == 5:
        print('5')
    elif A == 6:
        print('6')
    elif A == 7:
        if B % 4 == 1:
            print('7')
        elif B % 4 == 2:
            print('9')
        elif B % 4 == 3:
            print('3')
        else:
            print('1')
    elif A == 8:
        if B % 4 == 1:
            print('8')
        elif B % 4 == 2:
            print('4')
        elif B % 4 == 3:
            print('2')
        else:
            print('6')
    elif A == 9:
        if B % 2 == 1:
            print('9')
        else:
            print('1')
    else:
        print('10')

