from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
order = [0 for _ in range(N+1)]
Q = deque()
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    order[end] += 1
most_small = []
for i in range(1, len(order)):
    if not order[i]:
        Q.append(i)
answer = []
while Q:
    now = Q.popleft()
    answer.append(now)
    for node in graph[now]:
        order[node] -= 1
        if order[node] == 0:
            Q.append(node)

print(*answer)
