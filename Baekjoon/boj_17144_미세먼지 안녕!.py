def check_pm():
    for y in range(N):
        for x in range(M):
            if board[y][x] == -1:
                cleaner.append((y, x))
                continue
            if board[y][x] != 0:
                pm.append((y, x))

def split_pm():
    new_pm = []
    for y, x in pm:
        if board[y][x] < 5:
            continue
        sum_split = 0
        for i in range(4):
            ty = dy[i] + y
            tx = dx[i] + x
            if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
                continue
            if board[ty][tx] != -1:
                new_pm.append((ty, tx, int(board[y][x]/5)))
                sum_split += int(board[y][x]/5)
        board[y][x] -= sum_split

    for new_y, new_x, s_pm in new_pm:
        board[new_y][new_x] += s_pm

def up_clean(y, x):
    up_clean_list = []
    board[y][x] = 0
    while True:
        if x == M-1:
            break
        up_clean_list.append((y, x+1, board[y][x]))
        x += 1
    while True:
        if y == 0:
            break
        up_clean_list.append((y - 1, x, board[y][x]))
        y -= 1
    while True:
        if x == 0:
            break
        up_clean_list.append((y, x-1, board[y][x]))
        x -= 1
    while True:
        if y == cleaner[0][0] and x == cleaner[0][1]:
            break
        up_clean_list.append((y+1, x, board[y][x]))
        y += 1
    for move_y, move_x, move_pm in up_clean_list:
        board[move_y][move_x] = move_pm
    board[cleaner[0][0]][cleaner[0][1]] = -1

def down_clean(y, x):
    down_clean_list = []
    board[y][x] = 0
    while True:
        if x == M - 1:
            break
        down_clean_list.append((y, x + 1, board[y][x]))
        x += 1
    while True:
        if y == N-1:
            break
        down_clean_list.append((y + 1, x, board[y][x]))
        y += 1
    while True:
        if x == 0:
            break
        down_clean_list.append((y, x - 1, board[y][x]))
        x -= 1
    while True:
        if y == cleaner[1][0] and x == cleaner[1][1]:
            break
        down_clean_list.append((y - 1, x, board[y][x]))
        y -= 1
    for move_y, move_x, move_pm in down_clean_list:
        board[move_y][move_x] = move_pm
    board[cleaner[1][0]][cleaner[1][1]] = -1

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
N, M, T = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

for _ in range(T):
    pm = []
    cleaner = []
    check_pm()
    split_pm()
    up_clean(cleaner[0][0], cleaner[0][1])
    down_clean(cleaner[1][0], cleaner[1][1])

remain_pm = 0
for y in range(N):
    for x in range(M):
        if board[y][x] != -1:
            remain_pm += board[y][x]

print(remain_pm)