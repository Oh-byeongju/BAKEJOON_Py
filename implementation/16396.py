import sys
input = sys.stdin.readline

N = int(input())
text_lines = [0] * 10001
cnt = 0

for i in range(N):
    A, B = map(int, input().split())
    for j in range(A, B):
        text_lines[j] += 1

for i in range(len(text_lines)):
    if text_lines[i] >= 1:
        cnt += 1

print(cnt)
