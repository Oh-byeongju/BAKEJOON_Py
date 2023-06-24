import sys
input = sys.stdin.readline

while(True):
    try:
        A, B = map(int, input().split())
    except:
        break
    cnt = 0
    for i in range(A, B+1, 1):
        temp_list = []
        cnt += 1
        value = str(i)
        for j in range(len(value)):
            temp_list.append(value[j])
        for k in range(0, 10, 1):
            if temp_list.count(str(k)) >= 2:
                cnt -= 1
                break
    print(cnt)