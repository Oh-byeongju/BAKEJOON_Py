import sys
input = sys.stdin.readline

N = int(input())

round1 = list(map(int, input().split()))
round2 = list(map(int, input().split()))

cntA = 0
cntB = 0
temp = 0
result = 1

for i in range(N):
    if round1[i] == 1 and round2[i] == 3:
        cntA += 1
        result = max(result, cntA)
        cntB = 0
        temp = 1
    elif round1[i] == 3 and round2[i] == 1:
        cntB += 1
        result = max(result, cntB)
        cntA = 0
        temp = -1
    elif round1[i] > round2[i]:
        cntA += 1
        result = max(result, cntA)
        cntB = 0
        temp = 1
    elif round1[i] < round2[i]:
        cntB += 1
        result = max(result, cntB)
        cntA = 0
        temp = -1

    if round1[i] == round2[i]:
        if temp == 1:
            cntA = 0
            cntB = 1
            temp = -1
        elif temp == -1:
            cntA = 1
            cntB = 0
            temp = 1

print(result)

