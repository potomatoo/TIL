from collections import deque

N, M = map(int, input().split())
start_y, start_x = map(int, input().split())
goal_y, goal_x = map(int, input().split())
start_x, start_y = start_x-1, start_y-1
goal_x, goal_y = goal_x-1, goal_y-1
board = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
flag = False
for _ in range(N):
    board.append(list(map(int, input().split())))

visit = [[[0, 0] for _ in range(M)] for _ in range(N)]
Q = deque()
Q.append((start_y, start_x, 0, 0))
visit[start_y][start_x][0] = 1
answer = 0
while Q:
    now_y, now_x, p, d = Q.popleft()
    if now_y == goal_y and now_x == goal_x:
        answer = d
        flag = True
        break
    for i in range(4):
        ty = now_y + dy[i]
        tx = now_x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
            continue
        if board[ty][tx] == 0 and visit[ty][tx][p] == 0:
            visit[ty][tx][p] = 1
            Q.append((ty, tx, p, d + 1))

        elif board[ty][tx] == 1 and p == 0:
            visit[ty][tx][1] = 1
            Q.append((ty, tx, 1, d + 1))
for z in range(N):
    print(visit[z])
if flag:
    print(answer)
else:
    print(-1)
