doc = str(input())
word = str(input())
cnt = 0
temp = 0

while temp <= len(doc) - len(word):
    if doc[temp:temp + len(word)] == word:
        cnt += 1
        temp += len(word)
    else:
        temp += 1
print(cnt)