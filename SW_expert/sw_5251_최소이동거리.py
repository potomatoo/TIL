import sys
sys.stdin = open('./input/input_5251.txt', 'r')

TC = int(input())
for tc in range(TC):
    V, E = map(int,input().split())
    G = {i : [] for i in range(V+1)}
    for _ in range(E):
        s,e,c = map(int,input().split())
        G[s].append([e,c])

    INF = float('inf')
    dist = [INF] * (V+1)
    selected = [0] * (V+1)
    dist[0] = 0
    cnt = 0

    while cnt < V+1:
        MIN = INF
        u = -1
        for i in range(V+1):
            if not selected[i] and MIN > dist[i]:
                MIN = dist[i]
                u = i
        cnt += 1
        selected[u] = 1
        for w, cost in G[u]:
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost

    print('#{} {}'.format(tc+1, dist[V]))



