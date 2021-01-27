import heapq

def solution(n, s, a, b, fares):
    INF = 1e9
    graph = [[] for _ in range(n+1)]
    for start, end, cost in fares:
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    def djikstra(start, a, b, c):
        distance = [INF] * (n + 1)
        Q = []
        heapq.heappush(Q, (start, 0))
        distance[start] = 0
        while Q:
            now, now_cost = heapq.heappop(Q)
            if distance[now] < now_cost:
                continue
            for node, cost in graph[now]:
                new_cost = now_cost + cost
                if new_cost < distance[node]:
                    distance[node] = new_cost
                    heapq.heappush(Q, (node, new_cost))
        if c == 0:
            return distance
        return c + distance[a] + distance[b]

    distance = djikstra(s, a, b, 0)
    answer = distance[a] + distance[b]
    for k in range(1, len(distance)):
        if k == s:
            continue
        answer = min(answer, djikstra(k, a, b, distance[k]))

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))