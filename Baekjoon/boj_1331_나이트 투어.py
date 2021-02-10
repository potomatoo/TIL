alpha_dic = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5
}

dy = [2, 1, -1, -2, -2, -1, 1, 2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

behavior = []
for _ in range(36):
    behavior.append(input())

board = [[0 for _ in range(6)] for _ in range(6)]
now_y, now_x = 6 - int(behavior[0][1]), alpha_dic[behavior[0][0]]
flag = True
board[now_y][now_x] = 1
now = 2
for k in range(1, len(behavior)):
    y = 6 - int(behavior[k][1])
    x = alpha_dic[behavior[k][0]]
    mid_flag = False
    for i in range(8):
        ty = now_y + dy[i]
        tx = now_x + dx[i]
        if ty < 0 or ty > 5 or tx < 0 or tx > 5:
            continue
        if ty == y and tx == x and not board[ty][tx]:
            mid_flag = True
            board[ty][tx] = now
            now += 1
    if mid_flag:
        now_y, now_x = y, x
    else:
        print('Invalid')
        flag = False
        break

if flag:
    last_flag = False
    find_flag = False
    invalid_flag = False
    for y in range(6):
        for x in range(6):
            if board[y][x] == 36:
                now_y, now_x = y, x
                find_flag = True
                break
            if not board[y][x]:
                print('Invalid')
                invalid_flag = True
                break
        if find_flag or invalid_flag:
            break

    if not invalid_flag:
        for i in range(8):
            ty = now_y + dy[i]
            tx = now_x + dx[i]
            if ty < 0 or ty > 5 or tx < 0 or tx > 5:
                continue
            if board[ty][tx] == 1:
                last_flag = True
                print('Valid')
                break
        if not last_flag:
            print('Invalid')