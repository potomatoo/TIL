from collections import deque

def is_range(ty, tx):
    if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
        return False
    return True

def one_six(isGaro, one):
    if isGaro == 1:
        if garo[0][0] == 1 or garo[0][0] == 6:
            for i in range(4):
                if sero[i][0] == garo[0][0]:
                    sero[i] = (sero[i][0], one)
                    break
    else:
        if sero[0][0] == 1 or sero[0][0] == 6:
            for i in range(3):
                if garo[i][0] == sero[0][0]:
                    garo[i] = (garo[i][0], one)
                    break

def zero_case(order, ty, tx):
    isGaro = 1
    if order == 1:
        garo.rotate(1)
    elif order == 2:
        garo.rotate(-1)
    elif order == 3:
        sero.rotate(-1)
        isGaro = 0
    elif order == 4:
        sero.rotate(1)
        isGaro = 0

    if isGaro == 1:
        board[ty][tx] = garo[0][1]
        sero[0] = garo[0]
        sero[2] = garo[2]
        return garo[2][1]
    else:
        board[ty][tx] = sero[0][1]
        garo[0] = sero[0]
        garo[2] = sero[2]
        return sero[2][1]

def number_case(order, ty, tx):
    isGaro = 1
    if order == 1:
        garo.rotate(1)
        garo[0] = (garo[0][0], board[ty][tx])
    elif order == 2:
        garo.rotate(-1)
        garo[0] = (garo[0][0], board[ty][tx])
    elif order == 3:
        sero.rotate(-1)
        sero[0] = (sero[0][0], board[ty][tx])
        isGaro = 0
    elif order == 4:
        sero.rotate(1)
        sero[0] = (sero[0][0], board[ty][tx])
        isGaro = 0
    one_six(isGaro, board[ty][tx])
    board[ty][tx] = 0
    if isGaro == 1:
        sero[0] = garo[0]
        sero[2] = garo[2]
        return garo[2][1]
    else:
        garo[0] = sero[0]
        garo[2] = sero[2]
        return sero[2][1]

N, M, now_y, now_x, k = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
orders = list(map(int, input().split()))
garo = deque([(6, 0), (4, 0), (1, 0), (3, 0)])
sero = deque([(6, 0), (2, 0), (1, 0), (5, 0)])
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

for order in orders:
    ty = dy[order] + now_y
    tx = dx[order] + now_x
    if not is_range(ty, tx):
        continue
    if board[ty][tx] == 0:
        top = zero_case(order, ty, tx)
    else:
        top = number_case(order, ty, tx)

    print(top)
    now_y, now_x = ty, tx


