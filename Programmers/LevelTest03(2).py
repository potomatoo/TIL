import heapq

def solution(n, s, a, b, fares):
    answer = 0xffffff
    road = [[] for _ in range(n+1)]
    for start, end, cost in fares:
        road[start].append((end, cost))
        road[end].append((start, cost))

    def djikstra(start, a, b):
        INF = 1e9
        dist = [INF] * (n + 1)
        dist[start] = 0
        Q = []
        heapq.heappush(Q, (start, 0))
        while Q:
            now, now_cost = heapq.heappop(Q)
            if dist[now] < now_cost:
                continue
            for end, cost in road[now]:
                new_cost = now_cost + cost
                if new_cost < dist[end]:
                    dist[end] = new_cost
                    heapq.heappush(Q, (end, new_cost))
        if a == 0 and b == 0:
            return dist
        else:
            return dist[a] + dist[b]

    mid_dist = djikstra(s, 0, 0)

    for i in range(1, n+1):
        mid_answer = mid_dist[i]
        mid_answer += djikstra(i, a, b)
        answer = min(answer, mid_answer)

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))

