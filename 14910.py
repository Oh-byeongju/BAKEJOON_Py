import sys
input = sys.stdin.readline

Numbers = list(map(int, input().split()))

for i in range(len(Numbers)-1):
    if Numbers[i] <= Numbers[i+1]:
        continue
    else:
        print('Bad')
        exit()
print('Good')
