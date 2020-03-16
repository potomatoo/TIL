from collections import deque
M, N = map(int,input().split())
home = []
for _ in range(N):
    home.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
item = 0
s_y, s_x = 0, 0
for y in range(N):
    for x in range(M):
        if home[y][x] == 'S':
            s_y, s_x = y, x
        if home[y][x] == 'X':
            item += 1

cnt = item
visit2 = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(item+1):
    Q = deque()
    visit = [[0 for _ in range(M)] for _ in range(N)]
    D = [[0 for _ in range(M)] for _ in range(N)]
    Q.append((s_y, s_x))
    visit[s_y][s_x] = 1
    while Q:
        yy, xx = Q.popleft()
        if home[yy][xx] == 'X' and visit2[yy][xx] == 0:
            visit2[yy][xx] = 1
            ans += D[yy][xx]
            s_y, s_x = yy, xx
            cnt -= 1
            break
        if home[yy][xx] == 'E' and cnt == 0:
            ans += D[yy][xx]
            break
        for i in range(4):
            ty = yy + dy[i]
            tx = xx + dx[i]
            if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
                continue
            if home[ty][tx] != '#' and visit[ty][tx] == 0:
                visit[ty][tx] = 1
                Q.append((ty,tx))
                D[ty][tx] = D[yy][xx] + 1
print(ans)

