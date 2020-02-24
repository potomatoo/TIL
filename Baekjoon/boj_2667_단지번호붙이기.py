def dfs(y,x,cnt):
    visit[y][x] = 1
    d_map[y][x] = cnt
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N - 1 or tx > N - 1:
            continue
        while d_map[ty][tx] == 1 and visit[ty][tx] == 0:
            dfs(ty,tx,cnt)

N = int(input())
c_map = []
for i in range(N):
    c_map.append(input())
d_map = [[] for _ in range(N)]
for i in range(N):
    for j in c_map[i]:
        d_map[i].append(int(j))

visit = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = []
for y in range(N):
    for x in range(N):
        if d_map[y][x] == 1 and visit[y][x] == 0:
            cnt += 1
            dfs(int(y),int(x),cnt)
for i in range(1,cnt+1):
    c = 0
    for y in range(N):
        for x in range(N):
            if d_map[y][x] == i:
                c += 1
    result.append(c)
result.sort()
print(cnt)
for i in result:
    print(i)



