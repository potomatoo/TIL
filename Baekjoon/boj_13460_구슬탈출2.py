from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

red = blue = goal = tuple()
for y in range(N):
    for x in range(M):
        if board[y][x] == 'R':
            red = (y, x)
        elif board[y][x] == 'B':
            blue = (y, x)
        elif board[y][x] == 'O':
            goal = (y, x)
Q = deque()
visit = [[0] * M for _ in range(N)]
Q.append(red)
visit[red[0]][red[1]] = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

d = []
cnt = 0
while Q:
    y, x = Q.popleft()
    if y == goal[0] and x == goal[1]:
        print(visit[y][x]-1)
        print(cnt)
        break

    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
            continue
        if (board[ty][tx] == '.' or board[ty][tx] == 'O') and visit[ty][tx] == 0:

            if not d:
                d.append(i)
            elif d[-1] != i:
                d.append(i)
            visit[ty][tx] = visit[y][x] + 1
            Q.append((ty, tx))

for z in range(N):
    print(visit[z])
print(d)