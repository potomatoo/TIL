from _collections import deque

N, M = map(int,input().split())
lake = []
for _ in range(N):
    lake.append(list(map(str,[*input()])))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
swan = []
cnt = 0

while True:
    change = []
    for y in range(N):
        for x in range(M):
            if cnt == 0:
                if lake[y][x] == 'L':
                    swan.append((y, x))
            if lake[y][x] == 'X':
                for i in range(4):
                    ty = y + dy[i]
                    tx = x + dx[i]
                    if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
                        continue
                    if lake[ty][tx] == '.' or lake[ty][tx] == 'L':
                        change.append((y, x))
                        break
    for y, x in change:
        lake[y][x] = '.'

    Q = deque()
    Q.append((swan[0][0], swan[0][1]))
    visit = [[0 for _ in range(M)] for _ in range(N)]
    flag = True
    while Q:
        yy, xx = Q.popleft()
        if yy == swan[1][0] and xx == swan[1][1]:
            flag = False
            break
        for i in range(4):
            ty = yy + dy[i]
            tx = xx + dx[i]
            if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
                continue
            if (lake[ty][tx] == '.' or lake[ty][tx] == 'L') and visit[ty][tx] == 0:
                visit[ty][tx] = 1
                Q.append((ty, tx))
    cnt += 1

    if not flag:
        break
print(cnt)
