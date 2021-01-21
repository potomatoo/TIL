from collections import deque

def find_union(start_y, start_x):
    global flag
    Q = deque()
    Q.append((start_y, start_x, board[start_y][start_x], 1))
    visit.append((start_y, start_x))
    union = [board[start_y][start_x]]
    while Q:
        yy, xx, cost, d = Q.popleft()
        for i in range(4):
            ty = yy + dy[i]
            tx = xx + dx[i]
            if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                continue
            if (ty, tx) not in visit and L <= abs(board[yy][xx] - board[ty][tx]) <= R:
                visit.append((ty, tx))
                country_visit[ty][tx] = 1
                Q.append((ty, tx, cost + board[ty][tx], d+1))
                union.append(board[ty][tx])

    return union

N, L, R = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

answer = 0
while answer <= 2000:
    flag = 0
    country_visit = [[0 for _ in range(N)] for _ in range(N)]
    mid_board = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if country_visit[y][x]:
                continue
            visit = []
            union = find_union(y, x)
            if len(union) > 1:
                for ty, tx in visit:
                    mid_board[ty][tx] = sum(union) // len(union)
            else:
                mid_board[y][x] = board[y][x]
                flag += 1

    if flag == N * N:
        break
    board = mid_board
    answer += 1

print(answer)