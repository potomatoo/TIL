from collections import deque
from copy import deepcopy

def bfs(start_board):
    Q = deque()
    Q.append((start, start_board))
    result = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    while Q:
        now_s, board = Q.popleft()
        if board == result:
            return True
        for i in range(4):
            ty = now_s[0] + dy[i]
            tx = now_s[1] + dx[i]
            if ty < 0 or ty > 2 or tx < 0 or tx > 2:
                continue
            c_board = deepcopy(board)
            c_board[now_s[0]][now_s[1]], c_board[ty][tx] = c_board[ty][tx], c_board[now_s[0]][now_s[1]]
            Q.append(((ty, tx), c_board))
    return False


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
start_board = []
for _ in range(3):
    start_board.append(list(map(int, input().split())))
start = (0, 0)
for y in range(3):
    for x in range(3):
        if not start_board[y][x]:
            start = (y, x)

if bfs(start_board):
    print(1)
else:
    print(-1)
