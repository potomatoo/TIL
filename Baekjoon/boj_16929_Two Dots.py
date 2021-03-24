def find_cycle(y, x, d):
    global now_y, now_x, flag
    if y == now_y and x == now_x and d > 2:
        flag = True
        return
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
            continue
        if ty == now_y and tx == now_x and d < 2:
            continue
        if board[ty][tx] == board[now_y][now_x] and not visit[ty][tx]:
            visit[ty][tx] = 1
            find_cycle(y, x, d+1)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

flag = False
flag2 = False
for y in range(N):
    for x in range(M):
        visit = [[0 for _ in range(M)] for _ in range(N)]
        now_y, now_x = y, x
        find_cycle(y, x, 0)
        if flag:
            flag2 = True
            break
    if flag2:
        break

if flag2:
    print('Yes')
else:
    print('No')
