import sys
sys.setrecursionlimit(10**5)

def dfs(y, x, s, cnt):
    global ans, max_s

    if s == max_s:
        ans = min(ans, cnt)
        return
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        ss = s
        while 0 <= ty < N and 0 <= tx < M and board[ty][tx] == '.' and not visit[ty][tx]:
            visit[ty][tx] = 1
            ss += 1
            ty += dy[i]
            tx += dx[i]
        ty -= dy[i]
        tx -= dx[i]

        if ty == y and tx == x:
            continue
        dfs(ty, tx, ss, cnt+1)

        while ty != y or tx != x:
            visit[ty][tx] = 0
            ty -= dy[i]
            tx -= dx[i]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

TC = 1
while True:
    Input = input()
    if Input == '':
        break
    N, M = map(int, Input.split())
    board = []
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(N):
        board.append(input())

    ans = 1000000
    max_s = 0
    ball = []
    for y in range(N):
        for x in range(M):
            if board[y][x] == '.':
                ball.append((y, x))
                max_s += 1

    for y, x in ball:
        visit[y][x] = 1
        dfs(y, x, 1, 0)
        visit[y][x] = 0

    if ans == 1000000:
        ans = -1
    print('Case {}: {}'.format(TC, ans))
    TC += 1