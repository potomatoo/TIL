import sys
sys.stdin = open('./input/input_6057.txt','r')

TC = int(input())
for tc in range(TC):
    V, E = map(int,input().split())
    G = [[] for _ in range(V+1)]
    S = []
    for i in range(E):
        u, v = map(int,input().split())
        G[v].append(u)
        G[u].append(v)
    visit = [0 for _ in range(V+1)]
    v = 2
    visit[v] = 1
    print(v, end=' ')
    S.append(v)
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
