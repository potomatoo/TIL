import sys
sys.setrecursionlimit(1000000)
def dfs_R(y,x,cnt):
    visit[y][x] = 1
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
            continue
        while (r_map[ty][tx] == 'R' and visit[ty][tx] == 0):
            dfs_R(ty,tx,cnt)

def dfs_B(y,x,cnt):
    visit[y][x] = 1
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
            continue
        while (r_map[ty][tx] == 'B' and visit[ty][tx] == 0):
            dfs_B(ty,tx,cnt)
def dfs_G(y,x,cnt):
    visit[y][x] = 1
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
            continue
        while (r_map[ty][tx] == 'G' and visit[ty][tx] == 0):
            dfs_G(ty,tx,cnt)

def dfs_RG(y,x,cnt):
    visit[y][x] = 1
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
            continue
        while (r_map[ty][tx] == 'R' and visit[ty][tx] == 0) or (r_map[ty][tx] == 'G' and visit[ty][tx] == 0):
            dfs_RG(ty,tx,cnt)

N = int(input())
r_map = []
for _ in range(N):
    r_map.append(input())
visit = [[0 for _ in range(N)] for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
for y in range(N):
    for x in range(N):
        if r_map[y][x] == 'R' and visit[y][x] == 0:
            cnt += 1
            dfs_R(y,x,cnt)
        if r_map[y][x] == 'B' and visit[y][x] == 0:
            cnt += 1
            dfs_B(y,x,cnt)
        if r_map[y][x] == 'G' and visit[y][x] == 0:
           cnt += 1
           dfs_G(y,x,cnt)
print(cnt,end=' ')
cnt = 0
visit = [[0 for _ in range(N)] for _ in range(N)]
for y in range(N):
    for x in range(N):
        if (r_map[y][x] == 'R' and visit[y][x] == 0) or (r_map[y][x] == 'G' and visit[y][x] == 0):
            cnt += 1
            dfs_RG(y,x,cnt)
        if r_map[y][x] == 'B' and visit[y][x] == 0:
            cnt += 1
            dfs_B(y,x,cnt)
print(cnt)
