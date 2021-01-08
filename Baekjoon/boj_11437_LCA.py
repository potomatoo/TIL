import sys
sys.setrecursionlimit(100000)

def dfs(x, depth):
    visit[x] = 1
    d[x] = depth
    for i in graph[x]:
        if visit[i]:
            continue
        parent[i] = x
        dfs(i, depth+1)

def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    if a == b:
        return a
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

N = int(input())
parent = [0] * (N+1)
visit = [0] * (N+1)
d = [0] * (N+1)
graph = [[]for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))