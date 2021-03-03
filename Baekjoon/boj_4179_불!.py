from collections import deque

def bfs():
    global answer
    Q = deque()
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for fy, fx in fire:
        visit[fy][fx] = 1
        Q.append((fy, fx, 1, 0))
    Q.append((jy, jx, 0, 0))

    while Q:
        y, x, t, d = Q.popleft()
        if (y == 0 or x == 0 or y == N-1 or x == M-1) and t == 0:
            answer = d+1
            return True

        if t:
            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]
                if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
                    continue
                if board[ty][tx] != '#' and not visit[ty][tx]:
                    visit[ty][tx] = 1
                    Q.append((ty, tx, t, d+1))
        else:
            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]
                if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
                    continue
                if board[ty][tx] == '.' and not visit[ty][tx]:
                    visit[ty][tx] = 1
                    Q.append((ty, tx, t, d+1))
    return False

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0
N, M = map(int, input().split())
board = []
jy, jx = 0, 0
fire = []
for _ in range(N):
    board.append(input())

for y in range(N):
    for x in range(M):
        if board[y][x] == 'J':
            jy, jx = y, x
        elif board[y][x] == 'F':
            fire.append((y, x))

if bfs():
    print(answer)
else:
    print('IMPOSSIBLE')

