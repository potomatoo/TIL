N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append([m, s, d])

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    move = []
    for y in range(N):
        for x in range(N):
            if board[y][x]:
                for m, s, d in board[y][x]:
                    ty = (y + (dy[d]*s)) % N
                    tx = (x + (dx[d]*s)) % N
                    move.append([ty, tx, m, s, d])
                board[y][x] = []

    for ty, tx, m, s, d in move:
        board[ty][tx].append([m, s, d])

    move = []
    for y in range(N):
        for x in range(N):
            if len(board[y][x]) > 1:
                sum_m, sum_s = board[y][x][0][0], board[y][x][0][1]
                flag_odd_even = True
                if board[y][x][0][2] % 2:
                    check_odd_even = 1
                else:
                    check_odd_even = 0
                for i in range(1, len(board[y][x])):
                    if board[y][x][i][2] % 2 != check_odd_even:
                        flag_odd_even = False
                    sum_m += board[y][x][i][0]
                    sum_s += board[y][x][i][1]
                split_m = sum_m // 5
                split_s = sum_s // len(board[y][x])
                board[y][x] = []
                if split_m:
                    if flag_odd_even:
                        board[y][x].append([split_m, split_s, 0])
                        board[y][x].append([split_m, split_s, 2])
                        board[y][x].append([split_m, split_s, 4])
                        board[y][x].append([split_m, split_s, 6])
                    else:
                        board[y][x].append([split_m, split_s, 1])
                        board[y][x].append([split_m, split_s, 3])
                        board[y][x].append([split_m, split_s, 5])
                        board[y][x].append([split_m, split_s, 7])

answer = 0
for y in range(N):
    for x in range(N):
        if board[y][x]:
            for m, s, d in board[y][x]:
                answer += m
print(answer)