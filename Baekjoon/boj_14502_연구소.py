def dfs(y,x,cnt):
    visit[y][x] = 1
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
            continue
        while i_map[ty][tx] == 0 and visit[ty][tx] == 0:
            dfs(ty,tx,cnt)

N, M = map(int,input().split())
i_map = []
for _ in range(N):
    i_map.append(list(map(int,input().split())))
visit = [[0 for _ in range(M)]for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
for y in range(N):
    for x in range(M):
        if i_map[y][x] == 2 and visit[y][x] == 0:
            cnt += 1
            dfs(y,x,cnt)
print(cnt)
for y in range(N):
    print(visit[y])

