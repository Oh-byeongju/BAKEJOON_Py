import sys
input = sys.stdin.readline

n, q = map(int, input().split())

lists = list(map(int, input().split()))


for i in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        a, b = query[1]-1, query[2]
        print(sum(lists[a:b]))
        tempA = lists[a]
        tempB = lists[b-1]
        lists[a] = tempB
        lists[b-1] = tempA

    if query[0] == 2:
        a, b, c, d = query[1]-1, query[2], query[3]-1, query[4]
        sumAB = sum(lists[a:b])
        sumCD = sum(lists[c:d])
        print(sumAB - sumCD)
