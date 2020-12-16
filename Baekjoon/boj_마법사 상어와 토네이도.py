def flutter(y, x, flag):
    sum_sand = 0
    if flag == 0:
        move_point = board[y][x-1]
        if 0 <= y-1 < N:
            board[y-1][x] += int(move_point * 0.01)
            sum_sand += int(move_point * 0.01)
        if 0 <= y+1 < N:
            board[y + 1][x] += int(move_point * 0.01)
            sum_sand += int(move_point * 0.01)
        if 0 <= y-1 < N and 0 <= x-1 < N:
            board[y - 1][x - 1] += int(move_point * 0.07)
            sum_sand += int(move_point * 0.07)
        if 0 <= y+1 < N and 0 <= x-1 < N:
            board[y+1][x-1] += int(move_point * 0.07)
            sum_sand += int(move_point * 0.07)
        if 0 <= y-1 < N and 0 <= x-2 < N:
            board[y - 1][x - 2] += int(move_point * 0.1)
            sum_sand += int(move_point * 0.1)
        if 0 <= y+1 < N and 0 <= x-2 < N:
            board[y+1][x-2] += int(move_point * 0.1)
            sum_sand += int(move_point * 0.1)
        if 0 <= y-2 < N and 0 <= x-1 < N:
            board[y - 2][x - 1] += int(move_point * 0.02)
            sum_sand += int(move_point * 0.02)
        if 0 <= y+2 < N and 0 <= x-1 < N:
            board[y+2][x-1] += int(move_point * 0.02)
            sum_sand += int(move_point * 0.02)
        if 0 <= y < N and 0 <= x-3 < N:
            board[y][x-3] += int(move_point * 0.05)
            sum_sand += int(move_point * 0.05)
        if 0 <= x-2 < N:
            board[y][x-2] = move_point - sum_sand
    elif flag == 2:
        move_point = board[y][x + 1]
        if 0 <= y-1 < N:
            board[y-1][x] += int(move_point * 0.01)
            sum_sand += int(move_point * 0.01)
        if 0 <= y+1 < N:
            board[y + 1][x] += int(move_point * 0.01)
            sum_sand += int(move_point * 0.01)
        if 0 <= y-1 < N and 0 <= x+1 < N:
            board[y - 1][x + 1] += int(move_point * 0.07)
            sum_sand += int(move_point * 0.07)
        if 0 <= y+1 < N and 0 <= x+1 < N:
            board[y+1][x+1] += int(move_point * 0.07)
            sum_sand += int(move_point * 0.07)
        if 0 <= y-1 < N and 0 <= x+2 < N:
            board[y - 1][x + 2] += int(move_point * 0.1)
            sum_sand += int(move_point * 0.1)
        if 0 <= y+1 < N and 0 <= x+2 < N:
            board[y+1][x+2] += int(move_point * 0.1)
            sum_sand += int(move_point * 0.1)
        if 0 <= y-2 < N and 0 <= x+1 < N:
            board[y - 2][x + 1] += int(move_point * 0.02)
            sum_sand += int(move_point * 0.02)
        if 0 <= y+2 < N and 0 <= x+1 < N:
            board[y+2][x+1] += int(move_point * 0.02)
            sum_sand += int(move_point * 0.02)
        if 0 <= y < N and 0 <= x+3 < N:
            board[y][x+3] += int(move_point * 0.05)
            sum_sand += int(move_point * 0.05)
        if 0 <= x+2 < N:
            board[y][x+2] = move_point - sum_sand
    elif flag == 3:
        move_point = board[y-1][x]
        if 0 <= x - 1 < N:
            board[y][x-1] += int(move_point * 0.01)
            sum_sand += int(move_point * 0.01)
        if 0 <= x + 1 < N:
            board[y][x+1] += int(move_point * 0.01)
            sum_sand += int(move_point * 0.01)
        if 0 <= y - 1 < N and 0 <= x - 1 < N:
            board[y - 1][x - 1] += int(move_point * 0.07)
            sum_sand += int(move_point * 0.07)
        if 0 <= y - 1 < N and 0 <= x + 1 < N:
            board[y - 1][x + 1] += int(move_point * 0.07)
            sum_sand += int(move_point * 0.07)
        if 0 <= y - 2 < N and 0 <= x + 1 < N:
            board[y - 2][x + 1] += int(move_point * 0.1)
            sum_sand += int(move_point * 0.1)
        if 0 <= y - 2 < N and 0 <= x - 1 < N:
            board[y - 2][x - 1] += int(move_point * 0.1)
            sum_sand += int(move_point * 0.1)
        if 0 <= y - 1 < N and 0 <= x + 2 < N:
            board[y - 1][x + 2] += int(move_point * 0.02)
            sum_sand += int(move_point * 0.02)
        if 0 <= y - 1 < N and 0 <= x - 2 < N:
            board[y - 1][x - 2] += int(move_point * 0.02)
            sum_sand += int(move_point * 0.02)
        if 0 <= y - 3 < N:
            board[y-3][x] += int(move_point * 0.05)
            sum_sand += int(move_point * 0.05)
        if 0 <= y-2 < N:
            board[y-2][x] = move_point - sum_sand
    elif flag == 1:
        move_point = board[y-1][x]
        if 0 <= x - 1 < N:
            board[y][x-1] += int(move_point * 0.01)
            sum_sand += int(move_point * 0.01)
        if 0 <= x + 1 < N:
            board[y][x+1] += int(move_point * 0.01)
            sum_sand += int(move_point * 0.01)
        if 0 <= y + 1 < N and 0 <= x - 1 < N:
            board[y + 1][x - 1] += int(move_point * 0.07)
            sum_sand += int(move_point * 0.07)
        if 0 <= y + 1 < N and 0 <= x + 1 < N:
            board[y + 1][x + 1] += int(move_point * 0.07)
            sum_sand += int(move_point * 0.07)
        if 0 <= y + 2 < N and 0 <= x + 1 < N:
            board[y + 2][x + 1] += int(move_point * 0.1)
            sum_sand += int(move_point * 0.1)
        if 0 <= y + 2 < N and 0 <= x - 1 < N:
            board[y + 2][x - 1] += int(move_point * 0.1)
            sum_sand += int(move_point * 0.1)
        if 0 <= y + 1 < N and 0 <= x + 2 < N:
            board[y + 1][x + 2] += int(move_point * 0.02)
            sum_sand += int(move_point * 0.02)
        if 0 <= y + 1 < N and 0 <= x - 2 < N:
            board[y + 1][x - 2] += int(move_point * 0.02)
            sum_sand += int(move_point * 0.02)
        if 0 <= y + 3 < N:
            board[y+3][x] += int(move_point * 0.05)
            sum_sand += int(move_point * 0.05)
        if 0 <= y+2 < N:
            board[y+2][x] = move_point - sum_sand
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
print(board)
dy = [0, 1, 0, -1] * 10000
dx = [-1, 0, 1, 0] * 10000

start_y = start_x = int(N // 2)
cnt = 1
idx = 0
check_cnt = 0
while True:
    if start_y < 0 or start_x < 0:
        break
    if check_cnt == 2:
        cnt += 1
        check_cnt = 0
    check = idx % 4
    for _ in range(cnt):
        flutter(start_y, start_x, check)
        start_y = start_y + dy[idx]
        start_x = start_x + dx[idx]
    check_cnt += 1
    idx += 1
print(board)