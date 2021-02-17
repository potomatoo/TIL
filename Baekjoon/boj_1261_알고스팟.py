from collections import deque

M, N = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
Q = deque()
Q.append((0, 0))
visit = [[0 for _ in range(M)] for _ in range(N)]
visit[0][0] = 1
while Q:
    y, x = Q.popleft()
    if y == N-1 and x == M-1:
        print(visit[y][x]-1)
        break
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
            continue
        if not visit[ty][tx]:
            if board[ty][tx] == '1':
                visit[ty][tx] = visit[y][x] + 1
                Q.append((ty, tx))
            else:
                visit[ty][tx] = visit[y][x]
                Q.appendleft((ty, tx))




