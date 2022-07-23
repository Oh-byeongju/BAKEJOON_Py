import sys
input = sys.stdin.readline

temp_String = input()
result = []
cnt = 0

for i in range(len(temp_String) - 1):
    result.append(temp_String[i])

for i in range(3):
    result.append('*')

while(True):
    if len(result) == 3:
        break

    if result[0] == 'c' and result[1] == '=':
        cnt += 1
        result.pop(0)
        result.pop(0)
    elif result[0] == 'c' and result[1] == '-':
        cnt += 1
        result.pop(0)
        result.pop(0)
    elif result[0] == 'd' and result[1] == 'z' and result[2] == '=':
        cnt += 1
        result.pop(0)
        result.pop(0)
        result.pop(0)
    elif result[0] == 'd' and result[1] == '-':
        cnt += 1
        result.pop(0)
        result.pop(0)
    elif result[0] == 'l' and result[1] == 'j':
        cnt += 1
        result.pop(0)
        result.pop(0)
    elif result[0] == 'n' and result[1] == 'j':
        cnt += 1
        result.pop(0)
        result.pop(0)
    elif result[0] == 's' and result[1] == '=':
        cnt += 1
        result.pop(0)
        result.pop(0)
    elif result[0] == 'z' and result[1] == '=':
        cnt += 1
        result.pop(0)
        result.pop(0)
    else:
        cnt += 1
        result.pop(0)

print(cnt)