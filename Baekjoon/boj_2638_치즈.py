import sys
sys.setrecursionlimit(100000)

def dfs(y, x):
    c_map[y][x] = 2
    visit[y][x] = 1
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
            continue
        while c_map[ty][tx] == 0 and visit[ty][tx] == 0:
            dfs(ty, tx)

N, M = map(int,input().split())
c_map = []
for _ in range(N):
    c_map.append(list(map(int,input().split())))
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
time = 0
while True:
    visit = [[0 for _ in range(M)] for _ in range(N)]
    change_visit = [[0 for _ in range(M)] for _ in range(N)]
    dfs(0, 0)
    check_cheeze = 0
    for y in range(N):
        for x in range(M):
            if c_map[y][x] == 1:
                check_cheeze += 1
                change_visit[y][x] = 1
                cnt = 0
                for i in range(4):
                    ty = y + dy[i]
                    tx = x + dx[i]
                    if c_map[ty][tx] == 2 and change_visit[ty][tx] == 0:
                        cnt += 1
                    if cnt > 1:
                        c_map[y][x] = 2
                        break
    if check_cheeze == 0:
        break
    for y in range(N):
        for x in range(M):
            if c_map[y][x] == 2:
                c_map[y][x] = 0
    time += 1
print(time)
