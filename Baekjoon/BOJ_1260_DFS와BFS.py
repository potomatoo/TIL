from collections import deque

V, E, start = map(int,input().split())
G = [[] for _ in range(V+1)]
visit = [0] * (V+1)
for _ in range(E):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)
for i in range(1,len(G)):
    G[i].sort()

S = []
v = start
S.append(v)
print(v, end= ' ')
visit[v] = 1
while S:
    for w in G[v]:
        if visit[w]: continue
        S.append(v)
        visit[w] = 1
        print(w, end=' ')
        v = w
        break
    else:
        v = S.pop()
print()
Q = deque()
visit = [0] * (V+1)
v = start
Q.append(v)
print(v,end=' ')
visit[v] = 1
while Q:
    v = Q.popleft()
    for w in G[v]:
        if visit[w] == 1:
            continue
        Q.append(w)
        visit[w] = 1
        print(w,end=' ')
        v = w


