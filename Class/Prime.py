V, E = map(int,input().split())
adj = [[0] * V for _ in range(V)]
for i in range(E):
    s, e, c = map(int,input().split())
    adj[s][e] = c
    adj[e][s] = c

# key, p, mst 준비
INF = float('inf')
key = [INF] * V
p = [-1] * V
mst = [0] * V

# 시작점 선택: 0번 선택
key[0] = 0
cnt = 0
result = 0
while cnt < V:
    # 아직 mst가 아니고 key가 최소인 정점 선택 : u
    minium = INF
    u = -1
    for i in range(V):
        if not mst[i] and key[i] < minium:
            minium = key[i]
            u = i
    # u를 mst로 선택
    mst[u] = True
    result += minium
    cnt += 1
    # key값 갱신
    # u에 인접하고 아직 mst가 아닌 정점 w에서 key[w] > u-w 가중치면 갱신
    for w in range(V):
        if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
            key[w] = adj[u][w]
            p[w] = u


### 2번째 방법
import heapq
V, E = map(int,input().split())
adj = {i : [] for i in range(V)}
for i in range(E):
    s,e,c = map(int,input().split())
    adj[s].append([e,c])
    adj[e].append([s,c])

# key, mst, 우선순위큐 준비
INF = float('inf')
key = [INF] * V
mst = [False] * V
pq = []
# 시작 정점 선택 : 0
key[0] = 0
# 큐에 모든 정점을 넣음 => (key, 정점인덱스)
# 우선순위 큐 -> 이집힙 -> heapq 라이브러리 사용
heapq.heappush(pq, (0, 0))  # 우선순위큐-> 원소의 첫번째 요소 -> key를 우선순위로
result = 0
while pq:
    # 최소값 찾기
    k, node = heapq.heappop(pq)
    if mst[node] : continue  # old한 정보 스킵
    # mst로 선택
    mst[node] = True
    result += k
    # key값 갱신 => key배열/ 큐
    for dest, wt in adj[node]:
        if not mst[dest] and key[dest] > wt:
            key[dest] = wt
            # 큐 갱신 => 새로운 (key, 정점) 삽입 => 필요없는 원소는 스킵
            heapq.heappush(pq, (key[dest], dest))



