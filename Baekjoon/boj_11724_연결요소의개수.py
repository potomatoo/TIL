V, E = map(int,input().split())
G = [[]for _ in range(V+1)]
visit = [0] * (V+1)
S = []
for i in range(E):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)
cnt = 0
check = []
for i in range(1,V+1):
    if len(check) == V:
        break
    if i in check:
        continue
    cnt += 1
    v = i
    visit = [0] * (V+1)
    S.append(v)
    visit[v] = 1
    check.append(v)
    while S:
        for w in G[v]:
            if visit[w] == 1:
                continue
            visit[w] = 1
            check.append(w)
            S.append(v)
            v = w
            break
        else:
            v = S.pop()
print(cnt)
