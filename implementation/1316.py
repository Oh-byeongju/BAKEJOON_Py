import sys
input = sys.stdin.readline

cnt = 0
N = int(input())

for i in range(N):
    temp_result = []
    use_result = []
    word = input()

    for j in range(len(word) - 1):
        temp_result.append(word[j])

    alpha1 = temp_result[0]
    c_time = 0

    for res in temp_result:

        alpha2 = res

        if alpha1 != alpha2:
            use_result.append(alpha1)

        if alpha2 in use_result:
            break

        alpha1 = alpha2
        c_time += 1

        if c_time == len(word) - 1:
            cnt += 1

print(cnt)