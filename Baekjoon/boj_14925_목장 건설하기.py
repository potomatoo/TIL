M, N = map(int, input().split())
board = []
for _ in range(M):
    board.append(list(map(int, input().split())))
answer = 0
visit = [[0 for _ in range(N)] for _ in range(M)]
for y in range(M):
    for x in range(N):
        if board[y][x] == 1 or board[y][x] == 2:
            continue
        visit[y][x] = 1

for y in range(1, M):
    for x in range(1, N):
        if visit[y][x] >= 1:
            now = min(visit[y][x - 1], visit[y - 1][x], visit[y - 1][x - 1]) + 1
            visit[y][x] = now

for z in range(M):
    answer = max(max(visit[z]), answer)
print(answer)