import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

Numbers = [A,B,C,D,E]
Avg = 0

for i in Numbers:
    if i < 40:
        Avg += 40
    else:
        Avg += i

print(Avg//5)