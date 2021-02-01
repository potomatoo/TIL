import heapq
from itertools import permutations
def djikstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    distance = [INF] * (V+1)
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
    return distance
V, E = map(int, input().split())
INF = 1e9
graph = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

node = list(map(int, input().split()))
per_node = permutations(node, len(node))

answer = 1e9
for one in per_node:
    node = [1] + list(one) + [V]
    mid_answer = 0
    flag = True
    for i in range(len(node)-1):
        distance = djikstra(node[i])
        mid_cost = distance[node[i+1]]
        if mid_cost == 1e9:
            flag = False
            break
        mid_answer += mid_cost
    if flag:
        answer = min(answer, mid_answer)

if answer == 1e9:
    print(-1)
else:
    print(answer)
