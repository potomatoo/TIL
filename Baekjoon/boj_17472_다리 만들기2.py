def split_island(y, x):
    visit[y][x] = 1
    board[y][x] = island_number
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
            continue
        if board[ty][tx] == 1 and not visit[ty][tx]:
            split_island(ty, tx)

def find_bridge(y, x):
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        flag = False
        road = []
        while 0 <= ty < N and 0 <= tx < M:
            if board[ty][tx] == board[y][x]:
                break
            if board[ty][tx] != 0:
                flag = True
                break
            road.append((ty, tx))
            ty += dy[i]
            tx += dx[i]
        if flag:
            if len(road) < 2:
                continue
            road.sort(key=lambda x: [x[0], x[1]])
            if board[y][x] < board[ty][tx]:
                if (board[y][x], board[ty][tx], road, len(road)) not in bridge:
                    bridge.append((board[y][x], board[ty][tx], road, len(road)))
            else:
                if (board[ty][tx], board[y][x], road, len(road)) not in bridge:
                    bridge.append((board[ty][tx], board[y][x], road, len(road)))

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

island_number = 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visit = [[0 for _ in range(M)] for _ in range(N)]
for y in range(N):
    for x in range(M):
        if board[y][x] == 1 and not visit[y][x]:
            split_island(y, x)
            island_number += 1

bridge = []
for y in range(N):
    for x in range(M):
        if board[y][x] != 0:
            find_bridge(y, x)

bridge.sort(key=lambda x:x[3])

parent = [x for x in range(island_number)]
answer = 0
for start, end, road, d in bridge:
    if find_parent(parent, start) == find_parent(parent, end):
        continue
    union_parent(parent, start, end)
    answer += d

flag = True
check = find_parent(parent, 1)
for i in range(2, island_number):
    if check != find_parent(parent, i):
        flag = False
if answer and flag:
    print(answer)
else:
    print(-1)