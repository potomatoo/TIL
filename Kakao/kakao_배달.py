import heapq

def solution(N, road, K):
    def djikstra(start):
        Q = []
        heapq.heappush(Q, (0, start))
        distance[start] = 0
        while Q:
            dist, now = heapq.heappop(Q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(Q, (cost, i[0]))
    answer = 0
    INF = 1e9
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    djikstra(1)
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1
    print(distance)
    return answer

print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))