import heapq

def solution(N, road, K):
    answer = 0
    INF = 1e9
    graph = [[] for _ in range(N+1)]
    distance = [INF for _ in range(N+1)]
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    def djikstra(start):
        Q = []
        heapq.heappush(Q, (0, start))
        distance[start] = 0
        while Q:
            dist, now = heapq.heappop(Q)
            if dist > distance[now]:
                continue
            for node, cost in graph[now]:
                new_cost = cost + dist
                if new_cost < distance[node]:
                    distance[node] = new_cost
                    heapq.heappush(Q, (new_cost, node))
    djikstra(1)
    for i in distance:
        if i <= K:
            answer += 1
    return answer

print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))