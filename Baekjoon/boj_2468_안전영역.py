from sys import *
setrecursionlimit(10 ** 6)

def dfs(yy, xx, k):
    global cnt
    visit[yy][xx] = 1
    for i in range(4):
        ty = yy + dy[i]
        tx = xx + dx[i]
        if ty < 0 or ty > N-1 or tx < 0 or tx > N-1:
            continue
        if c_map[ty][tx] > k and visit[ty][tx] == 0:
            dfs(ty, tx, k)


N = int(input())
c_map = []
max_rain = 0
for i in range(N):
    one = list(map(int, input().split()))
    c_map.append(one)
    max_rain = max(max_rain, max(one))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0

for i in range(max_rain):
    visit = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if c_map[y][x] > i and visit[y][x] == 0:
                dfs(y, x, i)
                cnt += 1
    answer = max(answer, cnt)

print(answer)