from copy import deepcopy

def permutation(k):
    if k == 3:
        c_order = deepcopy(order)
        block.append(c_order)
    else:
        for i in range(len(clean)):
            if permutation_visit[i] == 1:
                continue
            permutation_visit[i] = 1
            order.append(clean[i])
            permutation(k+1)
            permutation_visit[i] = 0
            order.pop()

def dfs(y,x,lab):
    visit[y][x] = 1
    lab[y][x] = 2
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
            continue
        while lab[ty][tx] == 0 and visit[ty][tx] == 0:
            dfs(ty,tx,lab)

N, M = map(int,input().split())
lab = []
for _ in range(N):
    lab.append(list(map(int,input().split())))

clean = []
for y in range(N):
    for x in range(M):
        if lab[y][x] == 0:
            clean.append((y,x))
permutation_visit = [0] * len(clean)
order = []
block = []
permutation(0)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

max_cnt = 0

for i in range(len(block)):
    copy_lab = deepcopy(lab)
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for yy, xx in block[i]:
        copy_lab[yy][xx] = 1
    for y in range(N):
        for x in range(M):
            if copy_lab[y][x] == 2 and visit[y][x] == 0:
                dfs(y, x, copy_lab)
    cnt = 0
    for y in range(N):
        for x in range(M):
            if copy_lab[y][x] == 0:
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)









