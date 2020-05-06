import sys
sys.setrecursionlimit(100000)
from _collections import deque
from copy import deepcopy

def permutaion(k):
    if k == M:
        c_order = deepcopy(order)
        run_virus.append(c_order)
    else:
        for i in range(len(virus)):
            if visit[i] == 1:
                continue
            if len(order) > 0:
                if order[-1] > virus[i]:
                    continue
            visit[i] = 1
            order.append(virus[i])
            permutaion(k+1)
            visit[i] = 0
            order.pop()

N, M = map(int,input().split())
lab = []
for _ in range(N):
    lab.append(list(map(int,input().split())))

virus = []
for y in range(N):
    for x in range(N):
        if lab[y][x] == 2:
            virus.append((y, x))

visit = [0 for _ in range(len(virus))]
order = []
run_virus = []
permutaion(0)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans = 0xfffffff
for i in range(len(run_virus)):
    Q = deque()
    visit = [[0 for _ in range(N)] for _ in range(N)]
    D = [[0 for _ in range(N)] for _ in range(N)]
    for y, x in run_virus[i]:
        Q.append((y, x))
        visit[y][x] = 1
    while Q:
        yy, xx = Q.popleft()
        for ii in range(4):
            ty = yy + dy[ii]
            tx = xx + dx[ii]
            if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                continue
            if lab[ty][tx] != 1 and visit[ty][tx] == 0:
                visit[ty][tx] = 1
                Q.append((ty, tx))
                D[ty][tx] = D[yy][xx] + 1

    maxx = 0
    flag = True
    for y in range(N):
        if not flag:
            break
        for x in range(N):
            if D[y][x] == 0 and lab[y][x] == 0:
                flag = False
                break
            if maxx < D[y][x] and lab[y][x] != 2:
                maxx = D[y][x]
    if not flag:
        continue
    if ans > maxx:
        ans = maxx
if ans == 0xfffffff:
    print(-1)
else:
    print(ans)