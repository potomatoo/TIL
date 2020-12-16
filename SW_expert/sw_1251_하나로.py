import sys
sys.stdin = open('./input/input_1251.txt', 'r')

TC = int(input())
for tc in range(TC):
    V = int(input())
    adj = [[0] * V for _ in range(V)]
    island_x = list(map(int,input().split()))
    island_y = list(map(int,input().split()))
    g = float(input())
    island = []
    for i in range(V):
        island.append((island_x[i], island_y[i]))
    for i in range(len(island)-1):
        for j in range(i, len(island)):
            adj[i][j] = ((island[i][0] - island[j][0])**2 + (island[i][1] - island[j][1])**2) * g
            adj[j][i] = ((island[i][0] - island[j][0]) ** 2 + (island[i][1] - island[j][1]) ** 2) * g


    # key, p, mst 준비
    INF = float('inf')
    key = [INF] * V
    p = [-1] * V
    mst = [0] * V

    # 시작점 선택: 0번 선택
    key[0] = 0
    cnt = 0
    result = 0
    while cnt < V:
        # 아직 mst가 아니고 key가 최소인 정점 선택 : u
        minium = INF
        u = -1
        for i in range(V):
            if not mst[i] and key[i] < minium:
                minium = key[i]
                u = i
        # u를 mst로 선택
        mst[u] = True
        result += minium
        cnt += 1
        # key값 갱신
        # u에 인접하고 아직 mst가 아닌 정점 w에서 key[w] > u-w 가중치면 갱신
        for w in range(V):
            if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
                key[w] = adj[u][w]
                p[w] = u
    print('#{} {}'.format(tc+1, round(result)))





