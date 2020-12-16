from collections import deque
from copy import deepcopy
def permutation(k):
    if k == len(item_y_x):
        c_order = deepcopy(order)
        y_x.append(c_order + [(f_y, f_x)])
    else:
        for i in range(len(item_y_x)):
            if visited[i] == 1: continue
            visited[i] = 1
            order.append(item_y_x[i])
            permutation(k+1)
            visited[i] = 0
            order.pop()

M, N = map(int,input().split())
home = []
for _ in range(N):
    home.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

s_y, s_x = 0, 0
item_y_x = []
for y in range(N):
    for x in range(M):
        if home[y][x] == 'S':
            s_y, s_x = y, x
        if home[y][x] == 'X':
            item_y_x.append((y,x))
        if home[y][x] == 'E':
            f_y, f_x = y, x

order = []
visited = [0] * len(item_y_x)
y_x = []
permutation(0)

min_time = 0xfffffff
a, b = s_y, s_x
for per in range(len(y_x)):
    s_y, s_x = a, b
    time = 0
    for r, c in y_x[per]:
        Q = deque()
        Q.append((s_y, s_x, 0))
        visit = [[0 for _ in range(M)] for _ in range(N)]
        visit[s_y][s_x] = 1
        while Q:
            yy, xx, d = Q.popleft()
            if yy == r and xx == c:
                time += d
                s_y, s_x = yy, xx
            for i in range(4):
                ty = yy + dy[i]
                tx = xx + dx[i]
                if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
                    continue
                if home[ty][tx] != '#' and visit[ty][tx] == 0:
                    visit[ty][tx] = 1
                    Q.append((ty, tx, d+1))

    if time < min_time:
        min_time = time

print(min_time)