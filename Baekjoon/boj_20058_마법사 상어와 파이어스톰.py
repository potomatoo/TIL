import sys
sys.setrecursionlimit(10000)

def rotate(split_board):
    k = len(split_board)
    return_board = [[] for _ in range(k)]
    for y in range(k-1, -1, -1):
        for x in range(k):
            return_board[x].append(split_board[y][x])
    return return_board

def check_ice(y, x, s_board):
    k = len(s_board)
    check_cnt = 0
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty > k-1 or tx < 0 or tx > k-1:
            continue
        if s_board[ty][tx]:
            check_cnt += 1
    if check_cnt < 3:
        return False
    return True

def dfs(y, x, new_board, cnt):
    global max_ice
    k = len(new_board)
    visit[y][x] = cnt
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty > k-1 or tx < 0 or tx > k-1:
            continue
        if new_board[ty][tx] and not visit[ty][tx]:
            dfs(ty, tx, new_board, cnt)

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

n, q = map(int, input().split())
board = []
N = 2**n
for _ in range(N):
    board.append(list(map(int, input().split())))
levels = list(map(int, input().split()))

for level in levels:
    L = 2 ** level
    split_board = [[] for _ in range(N // L)]
    cnt = 0
    one = [[] for _ in range(N // L)]
    idx = 0
    for i in range(N):
        if cnt == L:
            split_board[idx] = one
            idx += 1
            one = [[] for _ in range(N // L)]
            cnt = 0
        t, k = 0, L
        for j in range(N//L):
            one[j].append(board[i][t:k])
            t += L
            k += L
        cnt += 1
        if i == N-1:
            split_board[idx] = one

    new_board = []
    for i in range(N//L):
        one = [[] for _ in range(L)]
        for j in range(N//L):
            split_board[i][j] = rotate(split_board[i][j])
            for y in range(L):
                for x in range(L):
                    one[y].append(split_board[i][j][y][x])
        for k in range(L):
            new_board.append(one[k])

    minus = []
    for y in range(N):
        for x in range(N):
            if not check_ice(y, x, new_board):
                minus.append((y, x))

    for y, x in minus:
        if new_board[y][x] == 0:
            continue
        new_board[y][x] -= 1

    remain_ice = 0
    max_ice = 0

    visit = [[0 for _ in range(N)] for _ in range(N)]

    cnt = 1
    for y in range(N):
        for x in range(N):
            if new_board[y][x] and not visit[y][x]:
                dfs(y, x, new_board, cnt)
                cnt += 1
            remain_ice += new_board[y][x]
    board = new_board

    max_ice_list = [0 for _ in range(cnt)]
    for y in range(N):
        for x in range(N):
            if not visit[y][x]:
                continue
            max_ice_list[visit[y][x]] += 1

print(remain_ice)
print(max(max_ice_list))
