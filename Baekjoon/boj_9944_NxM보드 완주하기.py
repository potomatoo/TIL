def dfs(y, x):
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
            continue
        if board[ty][tx] == '.' and not visit[ty][tx]:
            while True:
                if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
                    break
                if board[ty][tx] == '*' or visit[ty][tx]:
                    break
                visit[ty][tx] = 1
                ty += dy[i]
                tx += dx[i]
            ty -= dy[i]
            tx -= dx[i]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())
print(board)

ball = []
for y in range(N):
    for x in range(M):
        if board[y][x] == '.':
            ball.append((y, x))
print(ball)
visit = [[0 for _ in range(M)] for _ in range(N)]
dfs(0, 2)