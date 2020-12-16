def dfs(y, x):
    global cnt
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty > N-1 or tx < 0 or tx > N-1:
            continue
        if c_map[ty][tx] < N and visit[ty][tx] == 0:
            visit[ty][tx] = 1
            dfs(ty, tx)


N = int(input())
c_map = []
for i in range(N):
    c_map.append(list(map(int, input().split())))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visit = [[0 for _ in range(N)] for _ in range(N)]

cnt = 0

for y in range(N):
    for x in range(N):
        dfs(y, x)

print(cnt)