import sys
input = sys.stdin.readline

N = int(input())

def recur(num):
    S_array = ['***','* *','***']
    if num == 3:
        return S_array

    result = []
    temp_array = recur(num//3)

    for i in temp_array:
        result.append(i * 3)

    for i in temp_array:
        result.append(i + ' '*(num//3) + i)

    for i in temp_array:
        result.append(i * 3)
    return result

print('\n'. join(recur(N)))
