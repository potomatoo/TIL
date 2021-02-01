import heapq

def djikstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    distance[start] = 0
    while Q:
        dist, now = heapq.heappop(Q)
        if distance[now] < dist:
            continue
        for e, w in graph[now]:
            cost = dist + w
            if distance[e] > cost:
                distance[e] = cost
                heapq.heappush(Q, (cost, e))

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
start, end = map(int, input().split())
INF = 1e9
distance = [INF] * (N+1)
djikstra(start)
print(distance[end])
