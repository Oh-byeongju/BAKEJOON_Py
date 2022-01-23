import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    temp = int(input())
    if temp < 3:
        for j in range(temp):
            print('#' * temp)
        print()
    else:
        print('#' * temp)
        for j in range(temp-2):
            print('#' + 'J'*(temp-2) + '#')
        print('#' * temp, '\n')