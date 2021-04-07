def dfs(y, x, d):
    global answer, path
    if answer < d:
        answer = d
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
            continue
        if board[ty][tx] not in path:
            path += (board[ty][tx])
            dfs(ty, tx, d+1)
            path = path[:-1]


answer = 0
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

path = ''
path += board[0][0]
dfs(0, 0, 1)
print(answer)