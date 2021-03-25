import heapq

N = int(input())
graph = []

for _ in range(N):
    a, b = map(int, input().split())
    graph.append((a, b))

graph.sort(key=lambda x:x[0])

Q = []
for a, b in graph:
    if not Q:
        heapq.heappush(Q, b)
        continue
    if Q[0] <= a:
        heapq.heappop(Q)
        heapq.heappush(Q, b)
    else:
        heapq.heappush(Q, b)

print(len(Q))