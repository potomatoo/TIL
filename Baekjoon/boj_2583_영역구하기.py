import sys
sys.setrecursionlimit(100000)

def dfs(y,x,cnt):
    global width
    visit[y][x] = 1
    width += 1
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
            continue
        while c_map[ty][tx] == 0 and visit[ty][tx] == 0:
            dfs(ty,tx,cnt)

M, N, k = map(int,input().split())
c_map = [[0 for _ in range(M)]for _ in range(N)]
for _ in range(k):
    y1, x1, y2, x2 = map(int,input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            c_map[y][x] = 1

visit = [[0 for _ in range(M)]for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
ans = []
for y in range(N):
    for x in range(M):
        if c_map[y][x] == 0 and visit[y][x] == 0:
            cnt += 1
            width = 0
            dfs(y,x,cnt)
            ans.append(width)
ans.sort()
print(cnt)
print(*ans)

