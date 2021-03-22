from collections import deque

tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    E = K = G = (0, 0)
    for y in range(N):
        for x in range(M):
            if board[y][x] == 2:
                G = (y, x)
            elif board[y][x] == 3:
                E = (y, x)
            elif board[y][x] == 4:
                K = (y, x)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    Q = deque()
    Q.append(E)
    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit[E[0]][E[1]] = 1
    key_flag = False
    while Q:
        y, x = Q.popleft()
        if (y, x) == K:
            key_flag = True
            break
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
                continue
            if board[ty][tx] != 1 and not visit[ty][tx]:
                visit[ty][tx] = 1
                Q.append((ty, tx))
    if not key_flag:
        print(0)
    else:
        gold_flag = False
        Q = deque()
        Q.append(K)
        visit = [[0 for _ in range(M)] for _ in range(N)]
        visit[K[0]][K[1]] = 1
        while Q:
            y, x = Q.popleft()
            if (y, x) == G:
                gold_flag = True
                break
            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]
                if ty < 0 or ty > N - 1 or tx < 0 or tx > M - 1:
                    continue
                if board[ty][tx] != 1 and not visit[ty][tx]:
                    visit[ty][tx] = 1
                    Q.append((ty, tx))
        if gold_flag:
            print(1)
        else:
            print(0)