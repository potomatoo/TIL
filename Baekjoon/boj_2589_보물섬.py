from collections import deque

N, M = map(int,input().split())
world = []
for _ in range(N):
    world.append(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
ans = 0
for y in range(N):
    for x in range(M):
        if world[y][x] == 'L':
            Q = deque()
            Q.append((y, x, 0))
            visit = [[0 for _ in range(M)] for _ in range(N)]
            visit[y][x] = 1
            while Q:
                yy, xx, d = Q.popleft()
                for i in range(4):
                    ty = yy + dy[i]
                    tx = xx + dx[i]
                    if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
                        continue
                    if world[ty][tx] == 'L' and visit[ty][tx] == 0:
                        visit[ty][tx] = 1
                        Q.append((ty, tx, d+1))
            if ans < d:
                ans = d
print(ans)