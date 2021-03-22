# 시간 초과 및 실패!

def find_row_col(y, x):
    row = 0
    col = 0
    ty = y + 1
    while 0 <= ty < N and board[y][x] == board[ty][x]:
        row += 1
        ty += 1

    ty = y - 1
    while 0 <= ty < N and board[y][x] == board[ty][x]:
        row += 1
        ty -= 1

    tx = x + 1
    while 0 <= tx < N and board[y][x] == board[y][tx]:
        col += 1
        tx += 1

    tx = x - 1
    while 0 <= tx < N and board[y][x] == board[y][tx]:
        col -= 1
        tx -= 1

    return max(row, col) + 1

def find_max():
    now_max = 0
    for y in range(N):
        for x in range(N):
            now_max = max(now_max, find_row_col(y, x))
    return now_max

def find_near(y, x):
    near = []
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty > N-1 or tx < 0 or tx > N-1:
            continue
        near.append((ty, tx))
    return near

N = int(input())
board = []
for _ in range(N):
    line = ','.join(input())
    board.append(line.split(','))

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, 1, -1, -1, 1, -1, 1]

answer = 0
for y in range(N):
    for x in range(N):
        near = find_near(y, x)
        for ny, nx in near:
            board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
            now_max = find_max()
            answer = max(answer, now_max)
            board[y][x], board[ny][nx] = board[ny][nx], board[y][x]

print(answer)