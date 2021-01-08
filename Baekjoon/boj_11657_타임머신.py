def bf(x):
    distance[x] = 0
    for i in range(N):
        for j in range(M):
            start = graph[j][0]
            end = graph[j][1]
            cost = graph[j][2]
            if distance[start] != INF and distance[end] > cost + distance[start]:
                distance[end] = cost + distance[start]
                if i == N-1:
                    return True
    return False


INF = 1e9
N, M = map(int,input().split())
graph = []
distance = [INF] * (N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

nagative_cycle = bf(1)

if nagative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])

