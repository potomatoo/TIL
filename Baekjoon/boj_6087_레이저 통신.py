from collections import deque

def bfs(start_y, start_x, start_cost, start_d):
    Q = deque()
    Q.append((start_y, start_x, start_cost, start_d))
    visit = [[0 for _ in range(M)] for _ in range(N)]
    while Q:
        y, x, cost, d = Q.popleft()
        new_cost = 0
        if board[y][x] == 'C' and (y != start_y or x != start_x):
            answer.append(cost)
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or ty > N - 1 or tx < 0 or tx > M - 1:
                continue
            if d == i:
                new_cost = cost
            else:
                new_cost = cost + 1
            if board[ty][tx] != '*':
                if not visit[ty][tx] or visit[ty][tx] > new_cost:
                    visit[ty][tx] = new_cost
                    Q.append((ty, tx, new_cost, i))

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

M, N = map(int, input().split())
board = []
lazer = []
answer = []
for y in range(N):
    one = input()
    board.append(one)
flag = True
for yy in range(N):
    for xx in range(M):
        if board[yy][xx] == 'C':
            bfs(yy, xx, 0, 0)
            bfs(yy, xx, 0, 1)
            bfs(yy, xx, 0, 2)
            bfs(yy, xx, 0, 3)
            flag = False
            break
    if not flag:
        break
print(min(answer))

