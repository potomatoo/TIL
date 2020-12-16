def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x : return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1

V, E = map(int,input().split())
edges = [list(map(int,input().split())) for i in range(E)]
# 간선을 간선가중치를 기준으로 정렬
edges.sort(key=lambda x:x[2])
# make_set : 모든 정점에 대해 집합 생성
p = [0] * V
rank = [0] * V
for i in range(V):
    make_set(i)

cnt = 0
result = 0
mst = []
# 모든 간선에 대해서 반복 -> V-1개의 간선이 선택될때까지
for i in range(E):
    s, e, c = edges[i][0], edges[i][1], edges[i][2]
    # 싸이클이면 스킵 : 간선의 두 정점이 서로 같은 집합이면으로 사이클 확인 -> find_set
    if find_set(s) == find_set(e): continue
    # 싸이클이 아니면 간선 선택
    result += c
    mst.append(edges[i])
    # mst에 간선 정보 더하기 / 두 정점을 합친다 -> union
    union(s, e)
    cnt += 1
    if cnt == V-1:
        break

