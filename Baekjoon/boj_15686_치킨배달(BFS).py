from copy import deepcopy
from collections import deque

def permutation(k):
    if k == M:
        c_order = deepcopy(order)
        chicken.append(c_order)
    else:
        for i in range(len(w_chicken)):
            if visit[i] == 1: continue
            if len(order) > 0:
                if order[-1] > w_chicken[i]:
                    continue
            visit[i] = 1
            order.append(w_chicken[i])
            permutation(k+1)
            visit[i] = 0
            order.pop()

N, M = map(int,input().split())
street = []
for _ in range(N):
    street.append(list(map(int,input().split())))

w_chicken = []
for y in range(N):
    for x in range(N):
        if street[y][x] == 2:
            street[y][x] = 0
            w_chicken.append((y,x))

visit = [0 for _ in range(len(w_chicken))]
order = []
chicken = []
permutation(0)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

min_distance = 0xffffff

for k in range(len(chicken)):
    distance = 0
    for c_y, c_x in chicken[k]:
        street[c_y][c_x] = 2

    for r in range(N):
        for c in range(N):
            if street[r][c] == 1:
                Q = deque()
                visited = [[0 for _ in range(N)] for _ in range(N)]
                D = [[0 for _ in range(N)] for _ in range(N)]
                Q.append((r,c))
                visited[r][c] = 1
                while Q:
                    y, x = Q.popleft()
                    if street[y][x] == 2:
                        distance += D[y][x]
                        break
                    for i in range(4):
                        ty = y + dy[i]
                        tx = x + dx[i]
                        if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                            continue
                        if visited[ty][tx] == 0:
                            visited[ty][tx] = 1
                            Q.append((ty,tx))
                            D[ty][tx] = D[y][x] + 1

    if distance < min_distance:
        min_distance = distance
    for c_y, c_x in chicken[k]:
        street[c_y][c_x] = 0

print(min_distance)