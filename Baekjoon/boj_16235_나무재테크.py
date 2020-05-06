N, M, K = map(int,input().split())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

ground = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int,input().split())
    x = x - 1
    y = y - 1
    ground[y][x].append(z)

food = [[5 for _ in range(N)] for _ in range(N)]

dy = [-1, 1, 0, 0, -1, 1, -1, 1]
dx = [0, 0, -1, 1, 1, -1, -1, 1]

for _ in range(K):
    for y in range(N):
        for x in range(N):
            if ground[y][x]:
                ground[y][x].sort()
                live_tree, dead_tree = [], 0
                for t in range(len(ground[y][x])):
                    if food[y][x] >= ground[y][x][t]:
                        food[y][x] -= ground[y][x][t]
                        ground[y][x][t] += 1
                        live_tree.append(ground[y][x][t])
                    else:
                        dead_tree += ground[y][x][t] // 2
                food[y][x] += dead_tree
                ground[y][x] = []
                ground[y][x].extend(live_tree)

    for y in range(N):
        for x in range(N):
            food[y][x] += A[x][y]
            if ground[y][x]:
                for t in range(len(ground[y][x])):
                    if ground[y][x][t] % 5 == 0:
                        for ii in range(8):
                            ty = y + dy[ii]
                            tx = x + dx[ii]
                            if ty < 0 or tx < 0 or ty > N - 1 or tx > N - 1:
                                continue
                            ground[ty][tx].append(1)

cnt = 0
for y in range(N):
    for x in range(N):
        cnt += len(ground[y][x])
print(cnt)


