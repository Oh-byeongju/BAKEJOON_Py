import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
cnt = 0
graph = [[] * A for i in range(A + 1)]

for i in range(B):
    X, Y = map(int, input().split())
    graph[X].append(Y)
    graph[Y].append(X)

visited = [False] * (A + 1)

def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)


dfs(graph, 1, visited)
print(cnt)
