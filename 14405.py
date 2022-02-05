import sys
input = sys.stdin.readline

S = list(str(input().strip()))

for i in range(5001):
    if len(S) == 0:
        break
    elif len(S) == 1:
        break
    elif len(S) == 2:
        break

    if S[0] == 'p' and S[1] == 'i':
        S.remove(S[0])
        S.remove(S[0])
    elif S[0] == 'k' and S[1] == 'a':
        S.remove(S[0])
        S.remove(S[0])
    elif S[0] == 'c' and S[1] == 'h' and S[2] == 'u':
        S.remove(S[0])
        S.remove(S[0])
        S.remove(S[0])
    else:
        break

if len(S) == 0:
    print('YES')
elif len(S) == 1:
    print('NO')
elif S[0] == 'p' and S[1] == 'i':
    print('YES')
elif S[0] == 'k' and S[1] == 'a':
    print('YES')
else:
    print('NO')

