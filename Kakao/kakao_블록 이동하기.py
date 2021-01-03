# 미해결

from collections import deque

def solution(board):
    N = len(board)
    visit = [[0 for _ in range(N)] for _ in range(N)]
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]
    Q = deque()
    visit = [[0]*N for _ in range(N)]
    Q.append((0, 0, 0))
    Q.append((0, 1, 0))
    visit[0][0] = 1
    visit[0][1] = 1

    while Q:
        y, x, d = Q.popleft()
        if y == N - 1 and x == N-1:
            return d-1

        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or ty > N-1 or tx < 0 or tx > N-1:
                continue
            if not board[ty][tx] and not visit[ty][tx]:
                visit[ty][tx] = visit[y][x] + 1
                Q.append((ty, tx, visit[ty][tx]))


print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))