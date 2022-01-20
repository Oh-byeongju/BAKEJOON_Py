import sys
input = sys.stdin.readline

N = int(input())
data1 = list(map(int, input().split()))
if N > 1:
    data2 = list(map(int, input().split()))
value = 0

for i in range(N-1):
    value = max(value, data1[i]+data2[i])
    if value >= data1[i+1]:
        continue
    else:
        print('엄마 나 전역 늦어질 것 같아')
        exit()
print('권병장님, 중대장님이 찾으십니다')
