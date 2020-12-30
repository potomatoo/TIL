def split_sand(y, x, d):
    global out_sand
    move_sand = 0
    move_left = [(-1, 0, 0.07), (-2, 0, 0.02), (1, 0, 0.07), (2, 0, 0.02), (-1, 1, 0.01), (1, 1, 0.01), (-1, -1, 0.1),
                 (1, -1, 0.1), (0, -2, 0.05)]
    move_right = [(-1, 0, 0.07), (-2, 0, 0.02), (1, 0, 0.07), (2, 0, 0.02), (-1, -1, 0.01), (1, -1, 0.01), (-1, 1, 0.1),
                  (1, 1, 0.1), (0, 2, 0.05)]
    move_up = [(-1, -1, 0.1), (-1, 1, 0.1), (0, 1, 0.07), (0, -1, 0.07), (1, -1, 0.01), (1, 1, 0.01), (-2, 0, 0.05),
               (0, -2, 0.02), (0, 2, 0.02)]
    move_down = [(-1, -1, 0.01), (-1, 1, 0.01), (0, -1, 0.07), (0, 1, 0.07), (0, -2, 0.02), (0, 2, 0.02), (1, -1, 0.1),
                 (1, 1, 0.1), (2, 0, 0.05)]
    move_list = [move_left, move_down, move_right, move_up]
    alpha = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    for yy, xx, percent in move_list[d]:
        ty = yy + y
        tx = xx + x
        move_sand += int(board[y][x] * percent)
        if ty < 0 or ty > n-1 or tx < 0 or tx > n-1:
            out_sand += int(board[y][x] * percent)
            continue
        board[ty][tx] += int(board[y][x] * percent)

    alpha_y, alpha_x = y + alpha[d][0], x + alpha[d][1]
    if alpha_y < 0 or alpha_y > n-1 or alpha_x < 0 or alpha_x > n-1:
        out_sand += (board[y][x] - move_sand)
    else:
        board[alpha_y][alpha_x] += (board[y][x] - move_sand)

out_sand = 0
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

start_y, start_x = (n // 2), (n // 2)
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
idx = 0
cnt = 1
check_two = 0
flag = True

while True:
    for _ in range(cnt):
        start_y = start_y + dy[idx]
        start_x = start_x + dx[idx]
        split_sand(start_y, start_x, idx)
        if start_y == 0 and start_x == 0:
            flag = False
            break
    if not flag:
        break
    check_two += 1
    idx += 1
    if idx == 4:
        idx = 0
    if check_two == 2:
        check_two = 0
        cnt += 1

print(out_sand)