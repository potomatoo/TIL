N, M = map(int, input().split())

G = [[] for _ in range(N+1)]
visit = [0] * (N+1)
for _ in range(M):
    u, v, t = map(int,input().split())
    G[u].append(v)
for i in range(1, len(G)):
    G[i].sort()
print(G)





