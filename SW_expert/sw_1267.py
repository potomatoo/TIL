import sys
sys.stdin = open('./input/input_1267.txt','r')

for tc in range(10):
    V, E = map(int,input().split())
    G = [[] for _ in range(V+1)]
    visit = [0] * (V+1)
    S = []
    road = list(map(int,input().split()))
    print(road)
    for i in range(0,len(road)-1,2):
        G[road[i]].append(road[i+1])
    print(G)
    v = 1
    visit[v] = 1
    S.append(v)
    while S:
        for w in G[v]:
            if visit[w]: continue
            S.append(v)
            visit[w] = 1
            v = w
            break
        else:
            v = S.pop()
        


