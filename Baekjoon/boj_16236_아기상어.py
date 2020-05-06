from _collections import deque

N = int(input())
sea = []
for _ in range(N):
    sea.append(list(map(int,input().split())))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

shark_size = 2
size_gauge = 0

start = (0, 0, 0)
stop_find = False
for yy in range(N):
    for xx in range(N):
        if sea[yy][xx] == 9:
            start = (yy, xx, 0)
            stop_find = True
            break
    if stop_find:
        break

while True:
    GO = deque()
    GO.append(start)
    visit = [[0 for _ in range(N)] for _ in range(N)]
    visit[start[0]][start[1]] = 1
    EAT = []
    flag = True
    while GO:
        y, x, k = GO.popleft()

        if sea[y][x] != 0 and sea[y][x] < shark_size:
            GO.appendleft((y, x, k))
            for cy, cx, ck in GO:
                if ck > k:
                    flag = False
                    break
                if sea[cy][cx] != 0 and sea[cy][cx] < shark_size:
                    EAT.append((cy, cx, ck))
            flag = False
        if not flag:
            break

        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                continue
            if (sea[ty][tx] != 9 and sea[ty][tx] <= shark_size) and visit[ty][tx] == 0:
                visit[ty][tx] = 1
                GO.append((ty, tx, k+1))

    if not len(EAT):
        print(start[2])
        break

    if len(EAT) == 1:
        size_gauge += 1
        if size_gauge == shark_size:
            shark_size += 1
            size_gauge = 0
        sea[start[0]][start[1]] = 0
        sea[EAT[0][0]][EAT[0][1]] = 0
        start = (EAT[0][0], EAT[0][1], EAT[0][2])

    if len(EAT) > 1:
        size_gauge += 1
        EAT = sorted(EAT, key=lambda x: (x[0], x[1]))

        if size_gauge == shark_size:
            shark_size += 1
            size_gauge = 0
        sea[start[0]][start[1]] = 0
        sea[EAT[0][0]][EAT[0][1]] = 0
        start = (EAT[0][0], EAT[0][1], EAT[0][2])




