import heapq

def djikstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    distance[start] = 0
    while Q:
        now_cost, now = heapq.heappop(Q)
        if distance[now] < now_cost:
            continue
        for node, node_cost in graph[now]:
            new_cost = now_cost + node_cost
            if distance[node] > new_cost:
                distance[node] = new_cost
                heapq.heappush(Q, (new_cost, node))

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
INF = 1e9
distance = [INF] * (V+1)
djikstra(start)
for i in range(1, len(distance)):
    if distance[i] == INF:
        print('INF')
        continue
    print(distance[i])

