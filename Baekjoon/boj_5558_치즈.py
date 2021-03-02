from collections import deque

def bfs(y, x):
    global answer, now_y, now_x, now_n
    Q = deque()
    visit = [[0 for _ in range(W)] for _ in range(H)]
    Q.append((y, x))
    visit[y][x] = 1
    while Q:
        yy, xx = Q.popleft()
        if board[yy][xx].isnumeric() and int(board[yy][xx]) == now_n + 1:
            now_y, now_x, now_n = yy, xx, now_n+1
            answer += (visit[yy][xx]-1)
            break
        for i in range(4):
            ty = yy + dy[i]
            tx = xx + dx[i]
            if ty < 0 or ty > H-1 or tx < 0 or tx > W-1:
                continue
            if board[ty][tx] != 'X' and not visit[ty][tx]:
                visit[ty][tx] = visit[yy][xx] + 1
                Q.append((ty, tx))

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

answer = 0
H, W, N = map(int, input().split())
board = []
now_y, now_x, now_n = 0, 0, 0
for y in range(H):
    one = input()
    if 'S' in one:
        now_y, now_x = y, one.index('S')
    two = ','.join(one)
    board.append(two.split(','))

while N:
    bfs(now_y, now_x)
    N -= 1
print(answer)