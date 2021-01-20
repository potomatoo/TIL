def find_d(now_d, number, yy, xx):
    for i in range(4):
        ty = yy + dy[prefer_d[number][now_d][i]]
        tx = xx + dx[prefer_d[number][now_d][i]]
        if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
            continue
        if not board[ty][tx][0] and not board[ty][tx][1] and not board[ty][tx][2]:
            return prefer_d[number][now_d][i], number+1, ty, tx

    for i in range(4):
        ty = yy + dy[prefer_d[number][now_d][i]]
        tx = xx + dx[prefer_d[number][now_d][i]]
        if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
            continue
        if board[ty][tx][0] == -1 and board[ty][tx][1] == number+1:
            return prefer_d[number][now_d][i], number+1, ty, tx
    return now_d, number+1, yy, xx

def moving_shark():
    now_shark = []
    move_shark = []
    smell = []
    for y in range(N):
        for x in range(N):
            if not board[y][x][2]:
                continue
            if board[y][x][0] > 0:
                now_shark.append((y, x, board[y][x][0]))
                move_shark.append(find_d(board[y][x][1], board[y][x][0]-1, y, x))
            if board[y][x][0] == -1:
                smell.append((y, x, board[y][x][1], board[y][x][2]))

    for y, x, number, cost in smell:
        board[y][x] = (-1, number, cost-1)
        if not board[y][x][2]:
            board[y][x] = (0, 0, 0)

    for y, x, number in now_shark:
        board[y][x] = (-1, number, board[y][x][2]-1)
        if not board[y][x][2]:
            board[y][x] = (0, 0, 0)

    move_shark.sort(key=lambda x:x[1])
    visit = []
    new_shark = []
    for i in range(len(move_shark)):
        if (move_shark[i][2], move_shark[i][3]) in visit:
            continue
        new_shark.append(move_shark[i])
        visit.append((move_shark[i][2], move_shark[i][3]))

    for move_d, number, ty, tx in new_shark:
        board[ty][tx] = (number, move_d, k)


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M, k = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
start_d = list(map(int, input().split()))
prefer_d = []
one = []
for i in range(1, M*4+1):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        a[j] = a[j] - 1
    one.append(a)
    if not i % 4:
        prefer_d.append(one)
        one = []

for y in range(N):
    for x in range(N):
        if board[y][x]:
            board[y][x] = (board[y][x], start_d[board[y][x]-1]-1, k)
            continue
        board[y][x] = (0, 0, 0)

cnt = 0
flag = True
while True:
    cnt += 1
    if cnt > 1000:
        flag = False
        break
    moving_shark()

    check = 0
    for y in range(N):
        for x in range(N):
            if board[y][x][0] > 0:
                check += 1
    if check == 1:
        break

if flag:
    print(cnt)
else:
    print(-1)
