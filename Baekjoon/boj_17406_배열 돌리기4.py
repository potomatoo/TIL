from itertools import permutations
from copy import deepcopy
import sys
sys.setrecursionlimit(10**5)

def rotate(board, y, x, d):
    global start_y, end_y, start_x, end_x, after_cal, flag
    if not flag:
        return
    if y == (r-s-1 + r+s-1) // 2 and x == (c-s-1 + c+s-1) // 2:
        flag = False
        return
    if d == 3 and y == start_y and x == start_x:
        start_y, end_y, start_x, end_x = start_y+1, end_y-1, start_x+1, end_x-1
        rotate(board, y+1, x+1, 0)
    if flag:
        if (y == start_y and x == end_x) or (y == end_y and x == end_x) or (y == end_y and x == start_x):
            d += 1
        ty = y + dy[d]
        tx = x + dx[d]
        after_cal.append((ty, tx, board[y][x]))
        visit[ty][tx] = board[y][x]
        rotate(board, ty, tx, d)


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
N, M, K = map(int, input().split())
start_board = []
for _ in range(N):
    start_board.append(list(map(int, input().split())))

cal = []
for _ in range(K):
    cal.append(list(map(int, input().split())))

cal_per = permutations(cal, len(cal))
answer = 1e9
for one in cal_per:
    board = deepcopy(start_board)

    for r, c, s in one:
        start_y, end_y = r-s-1, r+s-1
        start_x, end_x = c-s-1, c+s-1
        visit = [[0 for _ in range(M)] for _ in range(N)]
        after_cal = []
        flag = True
        rotate(board, start_y, start_x, 0)
        for ty, tx, value in after_cal:
            board[ty][tx] = value

    mid_answer = 1e9
    for y in range(N):
        mid_answer = min(mid_answer, sum(board[y]))
    answer = min(answer, mid_answer)

print(answer)