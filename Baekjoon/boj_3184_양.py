from collections import deque

def bfs(start_y, start_x):
    global sheep, wolf
    Q = deque()
    Q.append((start_y, start_x))
    visit[start_y][start_x] = 1
    mid_sheep, mid_wolf = 0, 0
    while Q:
        now_y, now_x = Q.popleft()
        if board[now_y][now_x] == 'o':
            mid_sheep += 1
        elif board[now_y][now_x] == 'v':
            mid_wolf += 1
        for i in range(4):
            ty = now_y + dy[i]
            tx = now_x + dx[i]
            if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
                continue
            if not visit[ty][tx] and board[ty][tx] != '#':
                visit[ty][tx] = 1
                Q.append((ty, tx))
    if mid_sheep > mid_wolf:
        sheep += mid_sheep
    else:
        wolf += mid_wolf

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

sheep, wolf = 0, 0
visit = [[0 for _ in range(M)] for _ in range(N)]
for y in range(N):
    for x in range(M):
        if visit[y][x]: continue
        if board[y][x] == 'o' or board[y][x] == 'v':
            bfs(y, x)
print(sheep, wolf)