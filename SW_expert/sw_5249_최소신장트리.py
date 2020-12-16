import sys
sys.stdin = open('./input/input_5249.txt', 'r')

TC = int(input())
for tc in range(TC):
    V, E = map(int,input().split())
    G = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s,e,c = map(int,input().split())
        G[s][e] = c
        G[e][s] = c

    # p, mst, key 준비
    INF = float('inf')
    key = [INF] * (V+1)
    p = [-1] * (V+1)
    mst = [0] * (V+1)

    # 0번부터 시작
    key[0] = 0
    cnt = 0
    ans = 0
    while cnt < V+1:
        # 아직 mst가 아니고 가중치가 최소인 정점선택 : u
        minium = INF
        u = -1
        for i in range(V+1):
            if not mst[i] and minium > key[i]:
                minium = key[i]
                u = i
        # u를 mst로 선택
        mst[u] = 1
        cnt += 1
        ans += minium
        # u와 인접하고 아직 mst가 아닌 정점 w 중에서 가중치가 u-w보다 큰 값 갱신
        for w in range(V+1):
            if G[u][w] > 0 and not mst[w] and key[w] > G[u][w]:
                key[w] = G[u][w]
                p[w] = u

    print('#{} {}'.format(tc+1, ans))
