from copy import deepcopy
from itertools import combinations
def Go(board):
    for i in range(N):
        y = 0
        x = i
        while True:
            if y >= H:
                break
            if board[y][x][0] == 1:
                if x+1 < N:
                    if board[y][x+1][1] == x:
                        x += 1
                        y += 1
                        continue
                if 0 <= x-1:
                    if board[y][x-1][1] == x:
                        x -= 1
            y += 1
        if x != i:
            return False
    return True

N, M, H = map(int, input().split())
board = [[(0, 0) for _ in range(N)] for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = (1, b)
    board[a-1][b] = (1, b-1)

change_d = []
visit = [[0 for _ in range(N)] for _ in range(H)]
for y in range(H):
    for x in range(N):
        if board[y][x][0]:
            continue
        if x + 1 < N:
            if not board[y][x+1][0] and not visit[y][x+1]:
                change_d.append((y, x, x+1))
                visit[y][x] = 1
                visit[y][x+1] = 1
                continue
        if x - 1 >= 0:
            if not board[y][x-1][0] and not visit[y][x-1]:
                change_d.append((y, x-1, x))
                visit[y][x] = 1
                visit[y][x-1] = 1

visit = [0] * len(change_d)
order = []
#
# def dfs(k, many):
#     global answer
#     if k == many:
#         mid_board = deepcopy(board)
#         for height, left, right in order:
#             mid_board[height][left] = (1, right)
#             mid_board[height][right] = (1, left)
#         if Go(mid_board):
#             print(many)
#             sys.exit()
#         return
#     for i in range(len(change_d)):
#         if visit[i]: continue
#         if (change_d[i][0], change_d[i][1] - 1, change_d[i][1]) not in order and (change_d[i][0], change_d[i][2], change_d[i][2]+1) not in order:
#             visit[i] = 1
#             order.append(change_d[i])
#             dfs(k+1, many)
#             visit[i] = 0
#             order.pop()
answer = -1
def find(k):
    global answer
    com = list(combinations(change_d, k))
    for i in range(len(com)):
        flag = True
        for j in range(len(com[i])):
            if (com[i][j][0], com[i][j][1] - 1, com[i][j][1]) in com[i] or (com[i][j][0], com[i][j][2], com[i][j][2] + 1) in com[i]:
                flag = False
                break
        if flag:
            # mid_board = deepcopy(board)
            for height, left, right in com[i]:
                board[height][left] = (1, right)
                board[height][right] = (1, left)
            if Go(board):
                answer = k
                return
            for height, left, right in com[i]:
                board[height][left] = (0, 0)
                board[height][right] = (0, 0)

for i in range(4):
    if answer != -1:
        break
    find(i)
if answer != -1:
    print(answer)
else:
    print(-1)
