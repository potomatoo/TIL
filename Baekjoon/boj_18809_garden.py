from copy import deepcopy
from collections import deque

def permutation(k):
    if k == R+G:
        g_order = []
        r_order = []
        for i in range(len(order)):
            if i < G:
                c_order = deepcopy(order[i])
                g_order.append(c_order)
            else:
                c_order = deepcopy(order[i])
                r_order.append(c_order)
        G_loc.append(g_order)
        R_loc.append(r_order)

    else:
        for i in range(len(ground)):
            if g_visit[i]:
                continue
            g_visit[i] = 1
            order.append(ground[i])
            permutation(k+1)
            g_visit[i] = 0
            order.pop()




N, M, G, R = map(int,input().split())
garden = []
for _ in range(N):
    garden.append(list(map(int,input().split())))

# 씨를 뿌릴 수 있는 좌표
ground = []
for y in range(N):
    for x in range(M):
        if garden[y][x] == 2:
            ground.append((y,x))

order = []
g_visit = [0] * len(ground)
G_loc = []
R_loc = []

# 씨를 뿌릴 수 있는 좌표에서 순열생성
permutation(0)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

max_flower = 0
for k in range(len(G_loc)):
    c_garden = deepcopy(garden)
    Q = deque()
    D = [[0 for _ in range(M)] for _ in range(N)]
    for y, x in G_loc[k]:
        c_garden[y][x] = 3
        Q.append((y, x, 0))

    for y, x in R_loc[k]:
        c_garden[y][x] = 4
        Q.append((y, x, 0))

    flower = 0

    while Q:
        yy, xx, d = Q.popleft()
        for i in range(4):
            ty = yy + dy[i]
            tx = xx + dx[i]
            if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
                continue
            if D[ty][tx] == d+1:
                flower += 1
                continue
            if c_garden[ty][tx] == 1 or c_garden[ty][tx] == 2:
                c_garden[ty][tx] = c_garden[yy][xx]
                D[ty][tx] = d+1
                Q.append((ty, tx, d+1))

    if flower > max_flower:
        max_flower = flower

print(max_flower)