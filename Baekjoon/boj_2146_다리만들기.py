from collections import deque

N = int(input())
world = []
for _ in range(N):
    world.append(list(map(int,input().split())))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visit = [[0 for _ in range(N)] for _ in range(N)]
cnt = 1
for y in range(N):
    for x in range(N):
        if world[y][x] != 0 and visit[y][x] == 0:
            Q = deque()
            Q.append((y,x))
            visits = [[0 for _ in range(N)] for _ in range(N)]
            visits[y][x] = 1
            world[y][x] = cnt
            while Q:
                yy, xx = Q.popleft()
                for i in range(4):
                    ty = yy + dy[i]
                    tx = xx + dx[i]
                    if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                        continue
                    if world[ty][tx] != 0 and visits[ty][tx] == 0:
                        world[ty][tx] = cnt
                        visit[ty][tx] = 1
                        visits[ty][tx] = 1
                        Q.append((ty,tx))
            cnt += 1


for y in range(N):
    for x in range(N):
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                continue
            if world[y][x] != 0 and world[ty][tx] == 0:
                world[y][x] = -(world[y][x])
                break

ans = 0xffffffff
for y in range(N):
    for x in range(N):
        if world[y][x] < 0:
            Q = deque()
            Q.append((y, x, 0))
            visited = [[0 for _ in range(N)] for _ in range(N)]
            visited[y][x] = 1
            while Q:
                yy, xx, d = Q.popleft()
                if world[yy][xx] != 0 and world[yy][xx] != world[y][x]:
                    ans = min(ans, d-1)
                    break
                for i in range(4):
                    ty = yy + dy[i]
                    tx = xx + dx[i]
                    if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                        continue
                    if world[ty][tx] <= 0 and world[ty][tx] != world[y][x] and visited[ty][tx] == 0:
                        visited[ty][tx] = 1
                        Q.append((ty, tx, d+1))
print(ans)
