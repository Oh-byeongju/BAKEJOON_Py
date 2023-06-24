import sys
input = sys.stdin.readline

M, N = map(int, input().split())

def cal(n, q):
    temp = ''

    if n == 0:
        return '0'
    while n > 0:
        n, mod = divmod(n, q)
        if mod == 10:
            temp += str('A')
        elif mod == 11:
            temp += str('B')
        elif mod == 12:
            temp += str('C')
        elif mod == 13:
            temp += str('D')
        elif mod == 14:
            temp += str('E')
        elif mod == 15:
            temp += str('F')
        else:
            temp += str(mod)

    return temp[::-1]

print(cal(M, N))
