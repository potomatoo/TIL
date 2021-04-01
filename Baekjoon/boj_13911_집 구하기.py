import heapq

def djikstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    distance = [INF] * (V + 3)
    distance[start] = 0
    while Q:
        now_cost, now = heapq.heappop(Q)
        if distance[now] < now_cost:
            continue
        for past_cost, node in graph[now]:
            new_cost = past_cost + now_cost
            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(Q, (new_cost, node))
    return distance

V, E = map(int, input().split())
graph = [[] for _ in range(V+3)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

M, x = map(int, input().split())
mac = list(map(int, input().split()))

S, y = map(int, input().split())
star = list(map(int, input().split()))

INF = 1e9
for m in mac:
    graph[V+1].append((0, m))
for s in star:
    graph[V+2].append((0, s))
    # G[s].append((V+1, 0))

    # G[m].append((V+2, 0))

mac_dist = djikstra(V+1)
star_dist = djikstra(V+2)

answer = 1e9

for i in range(1, V+1):
    if i in star or i in mac: continue
    if star_dist[i] > y or mac_dist[i] > x: continue
    answer = min(answer, star_dist[i] + mac_dist[i])

if answer == 1e9:
    print(-1)
else:
    print(answer)