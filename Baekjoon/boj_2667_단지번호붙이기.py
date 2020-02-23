def dfs(x,y,cnt):
    if x == N-1 and y == N-1:
        return
    visited[y][x] = 1
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]
                if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                    continue
                while d_map[ty][tx] == 1 and visited[ty][tx] == 0:
                    if dfs(ty,tx,cnt+1):
                        return 1

N = int(input())
d_map = []
for _ in range(N):
    d_map.append(input())
visited = [[0 for _ in range(N)] for _ in range(N)]
S = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
print(dfs(0,0,0))