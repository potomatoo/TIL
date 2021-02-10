def solution(N, road, K):
    answer = 0
    INF = 1e9
    graph = [[INF]*(N+1) for _ in range(N+1)]
    for a, b, cost in road:
        if cost < graph[a][b]:
            graph[a][b] = cost
        if cost < graph[b][a]:
            graph[b][a] = cost

    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                if a == b:
                    graph[a][b] = 0
                else:
                    graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    for i in graph[1]:
        if i <= K:
            answer += 1
    print(graph[1])
    return answer

print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))