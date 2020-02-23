V = int(input())
E = int(input())
G = [[] for _ in range(V+1)]
visit = [0] * (V+1)
for i in range(E):
    v, u = map(int,input().split())
    G[v].append(u)
    G[u].append(v)

v = 1
visit[v] = 1
S = []
cnt = 0
S.append(v)
while S:
    for w in G[v]:
        if visit[w]: continue
        visit[w] = 1
        S.append(v)
        cnt += 1
        v = w
        break
    else:
        v = S.pop()
print(cnt)