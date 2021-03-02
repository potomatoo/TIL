import sys
sys.setrecursionlimit(10**5)

def find_island(y, x):
    for i in range(8):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty > h-1 or tx < 0 or tx > w-1:
            continue
        if board[ty][tx] and not visit[ty][tx]:
            visit[ty][tx] = 1
            find_island(ty, tx)

dy = [0, 0, -1, 1, -1, -1, 1, 1]
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))
    visit = [[0 for _ in range(w)] for _ in range(h)]
    answer = 0
    for y in range(h):
        for x in range(w):
            if board[y][x] and not visit[y][x]:
                find_island(y, x)
                answer += 1
    print(answer)