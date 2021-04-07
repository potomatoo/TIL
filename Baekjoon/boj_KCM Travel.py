import heapq

def djikstra(start):
    Q = []
    heapq.heappush(Q, (0, start, 0))
    distance[start] = 0
    while Q:
        now_time, now, now_cost = heapq.heappop(Q)
        if now_time > distance[now]:
            continue
        for node, past_cost, past_time in graph[now]:
            new_cost = now_cost + past_cost
            new_time = now_time + past_time
            if new_cost <= M and new_time < distance[node]:
                distance[node] = new_time
                heapq.heappush(Q, (new_time, node, new_cost))

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        start, end, cost, d = map(int, input().split())
        graph[start].append((end, cost, d))

    INF = 1e9
    distance = [INF] * (N+1)
    djikstra(1)
    print(distance)
    if distance[N] == 1e9:
        print('Poor KCM')
    else:
        print(distance[N])