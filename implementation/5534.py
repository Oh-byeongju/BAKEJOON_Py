import sys
input = sys.stdin.readline

def check(string):
    for i in range(len(string)):
        if string[i] == name[0]:
            for j in range(i, len(string)):
                if string[j] == name[-1]:
                    avg = (j-i)//(M-1)
                    temp = 0
                    while temp < M:
                        if string[i+avg*temp] == name[temp]:
                            temp += 1
                            continue
                        break
                    else:
                        return 1
    return 0

N = int(input())
name = input().strip()
M = len(name)
texts = list(input().strip() for _ in range(N))
cnt = 0
for text in texts:
    cnt += check(text)
print(cnt)