N, M = map(int,input().split())
castle = [list(map(str,[*input()])) for _ in range(N)]
search = []
for y in range(N):
    for x in range(M):
        if castle[y][x] != '.' and castle[y][x] != '9':
            castle[y][x] = int(castle[y][x])
            search.append((y, x, 0, 0))

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, 1, -1]

for y in range(N):
    for x in range(M):
        if castle[y][x] != '.' and castle[y][x] != '9':
            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]
                if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
                    continue
                if castle[ty][tx] == '.':
                    search
