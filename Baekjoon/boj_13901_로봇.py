import sys
sys.setrecursionlimit(10**5)

def move_robot(y, x, k):
    cnt = 0
    visit[y][x] = 1
    while True:
        if cnt == 4:
            break
        if k == 4:
            k = 0
        ty = y + dy[d[k]-1]
        tx = x + dx[d[k]-1]
        if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
            k += 1
            cnt += 1
            continue
        if board[ty][tx] or visit[ty][tx]:
            k += 1
            cnt += 1
            continue
        if not board[ty][tx] or not visit[ty][tx]:
            visit[ty][tx] = 1
            y, x = ty, tx
            cnt = 0
    return y, x

N, M = map(int, input().split())
K = int(input())
board = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    br, bc = map(int, input().split())
    board[br][bc] = 1

start_y, start_x = map(int, input().split())
visit = [[0 for _ in range(M)] for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
d = list(map(int, input().split()))
y, x = move_robot(start_y, start_x, 0)
print(y, x)
