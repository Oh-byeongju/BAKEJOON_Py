import sys
input = sys.stdin.readline

S = input()
result = set()

for i in range(len(S)-1):
    for j in range(i, len(S)-1):
        temp = S[i:j+1]
        result.add(temp)

print(len(result))
