from collections import deque

N, M = map(int,input().split())
bing = []
for _ in range(N):
    bing.append(list(map(int,input().split())))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

year = 0
while True:
    year += 1

    visit = [[0 for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if bing[y][x] > 0:
                visit[y][x] = 1
                cnt = 0
                for i in range(4):
                    ty = y + dy[i]
                    tx = x + dx[i]
                    if ty < 0 or tx < 0 or ty > N - 1 or tx > M - 1:
                        continue
                    if bing[ty][tx] == 0 and visit[ty][tx] == 0:
                        cnt += 1
                bing[y][x] = bing[y][x] - cnt
                if bing[y][x] < 0:
                    bing[y][x] = 0

    zero = 0
    for y in range(N):
        for x in range(M):
            if bing[y][x] != 0:
                zero += 1

    if zero == 0:
        year = 0
        break

    k = 0
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if bing[y][x] != 0 and visit[y][x] == 0:
                k += 1
                Q = deque()
                Q.append((y, x))
                visit[y][x] = 1
                while Q:
                    yy, xx = Q.popleft()
                    for i in range(4):
                        ty = yy + dy[i]
                        tx = xx + dx[i]
                        if ty < 0 or tx < 0 or ty > N - 1 or tx > M - 1:
                            continue
                        if bing[ty][tx] != 0 and visit[ty][tx] == 0:
                            visit[ty][tx] = 1
                            Q.append((ty, tx))
    if k >= 2:
        break

print(year)






