# 실패!

import sys
sys.setrecursionlimit(10**5)
from copy import deepcopy

def change_area(y, x, idx, board):
    cnt = 7
    while cnt:
        ty = dy[idx] + y
        tx = dx[idx] + x
        if (ty < 0 or tx < 0 or ty > 3 or tx > 3) or board[ty][tx][0] == -1:
            if idx == 7:
                idx = 0
            else:
                idx += 1
        else:
            break
        cnt -= 1

    if cnt:
        board[y][x], board[ty][tx] = board[ty][tx], (board[y][x][0], idx+1)

def move_fish(board):
    for i in range(1, 17):
        flag = True
        for y in range(4):
            for x in range(4):
                if board[y][x][0] == i:
                    change_area(y, x, board[y][x][1]-1, board)
                    flag = False
                    break
            if not flag:
                break

def can_eat(y, x, board):
    eat = []
    idx = board[y][x][1]-1
    while True:
        ty = y + dy[idx]
        tx = x + dx[idx]
        if ty < 0 or tx < 0 or ty > 3 or tx > 3:
            break
        if board[ty][tx][0] == 0:
            continue
        eat.append((ty, tx))
        y, x = ty, tx
    return eat

def move_shark(y, x, cost, board):
    global answer
    board = deepcopy(board)
    now_fish = board[y][x][0]
    board[y][x] = (-1, board[y][x][1])

    move_fish(board)
    eat = can_eat(y, x, board)
    answer = max(answer, cost+now_fish)
    for ny, nx in eat:
        move_shark(ny, nx, cost+now_fish, board)


board = [[] for _ in range(4)]
for i in range(4):
    one = list(map(int, input().split()))
    for j in range(0, len(one)-1, 2):
        board[i].append((one[j], one[j+1]))
answer = 0
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
move_shark(0, 0, 0, board)
for z in range(4):
    print(board[z])
print()
print(answer)
