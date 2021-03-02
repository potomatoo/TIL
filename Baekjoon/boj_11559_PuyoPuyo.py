from collections import deque

def bfs(y, x, color):
    Q = deque()
    visit = [[0 for _ in range(6)] for _ in range(12)]
    Q.append((y, x))
    visit[y][x] = 1
    remove = [(y, x)]
    cnt = 1
    while Q:
        now_y, now_x = Q.popleft()
        for i in range(4):
            ty = now_y + dy[i]
            tx = now_x + dx[i]
            if ty < 0 or ty > 11 or tx < 0 or tx > 5:
                continue
            if board[ty][tx] == color and not visit[ty][tx]:
                visit[ty][tx] = 1
                remove.append((ty, tx))
                cnt += 1
                Q.append((ty, tx))
    if cnt >= 4:
        for yy, xx in remove:
            board[yy][xx] = '.'
        return True
    return False

def go_down():
    mid_board = []
    for x in range(6):
        mid = []
        for y in range(12):
            mid.append(board[y][x])
        mid_board.append(mid)

    new_board = []
    for z in range(6):
        mid = deque()
        for i in range(len(mid_board[z])):
            if mid_board[z][i] == '.':
                mid.appendleft(mid_board[z][i])
            else:
                mid.append(mid_board[z][i])
        new_board.append(list(mid))

    return_board = []
    for x in range(12):
        mid = []
        for y in range(6):
            mid.append(new_board[y][x])
        return_board.append(mid)

    return return_board

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

N, M = 12, 6
board = []
for _ in range(12):
    one = ','.join(input())
    board.append(one.split(','))

answer = 0
while True:
    flag = True
    for y in range(12):
        for x in range(6):
            if board[y][x] == '.':
                continue
            if bfs(y, x, board[y][x]):
                flag = False
    if not flag:
        board = go_down()
        answer += 1

    else:
        break
print(answer)