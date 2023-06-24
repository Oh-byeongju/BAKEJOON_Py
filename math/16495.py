import sys
input = sys.stdin.readline

Texts = list(map(str, input().strip()))
Num = 0
temp = len(Texts)

if temp == 1:
    print(ord(Texts[0])-64)
    exit()

for i in range(0, temp, 1):
    if i == temp-1:
        Num += (ord(Texts[i])-64)
    else:
        Num += (ord(Texts[i])-64) * (26 ** (temp-1-i))

print(Num)
