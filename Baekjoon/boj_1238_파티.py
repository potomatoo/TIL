import heapq

def djikstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    cost = [INF] * (N + 1)
    cost[start] = 0
    while Q:
        now_cost, now = heapq.heappop(Q)
        if cost[now] < now_cost:
            continue
        for node, c in graph[now]:
            new_cost = now_cost + c
            if new_cost < cost[node]:
                cost[node] = new_cost
                heapq.heappush(Q, (new_cost, node))
    return cost


N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
INF = int(1e9)

answer = 0

for i in range(1, N+1):
    if i == X:
        continue
    answer = max(answer, djikstra(i)[X] + djikstra(X)[i])

print(answer)