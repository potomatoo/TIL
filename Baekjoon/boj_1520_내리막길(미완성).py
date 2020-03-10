def dfs(y,x):
    global ans

    if y == N-1 and x == M-1:
        ans += 1
        return
    visit[y][x] = 1
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
            continue
        if mountain[ty][tx] < mountain[y][x] and visit[ty][tx] == 0:
            dfs(ty,tx)
            visit[ty][tx] = 0


N, M = map(int,input().split())
mountain = []
for _ in range(N):
    mountain.append(list(map(int,input().split())))
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visit = [[0 for _ in range(M)]for _ in range(N)]
ans = 0
dfs(0,0)
print(ans)