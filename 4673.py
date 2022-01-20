import sys
input = sys.stdin.readline

no_self = []

def cal(A):
    result = int(A)
    # 길이만큼 반복
    for i in list(str(A)):
        result += int(i)
    return result

for i in range(1, 10001):
    temp = cal(i)
    no_self.append(temp)

for i in range(1, 10001):
    if i not in no_self:
        print(i)
