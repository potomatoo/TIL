from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
dk = [-1, 1]

while True:
    K, N, M = map(int, input().split())
    if K == 0 and N == 0 and M == 0:
        break
    board = []
    for _ in range(K):
        one = []
        for _ in range(N):
            one.append(input())
        input()
        board.append(one)

    start = (0, 0, 0, 0)
    end = (0, 0, 0)
    for i in range(K):
        for y in range(N):
            for x in range(M):
                if board[i][y][x] == 'S':
                    start = (i, y, x, 0)
                if board[i][y][x] == 'E':
                    end = (i, y, x)

    visit = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K)]
    Q = deque()
    Q.append(start)
    visit[start[0]][start[1]][start[2]] = 1
    answer = 0
    while Q:
        now_k, now_y, now_x, d = Q.popleft()
        if now_k == end[0] and now_y == end[1] and now_x == end[2]:
            answer = d
            break
        for i in range(4):
            ty = now_y + dy[i]
            tx = now_x + dx[i]
            if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
                continue
            if board[now_k][ty][tx] != '#' and not visit[now_k][ty][tx]:
                visit[now_k][ty][tx] = 1
                Q.append((now_k, ty, tx, d+1))
        for i in range(2):
            tk = now_k + dk[i]
            if tk < 0 or tk > K-1:
                continue
            if board[tk][now_y][now_x] != '#' and not visit[tk][now_y][now_x]:
                visit[tk][now_y][now_x] = 1
                Q.append((tk, now_y, now_x, d+1))

    if not answer:
        print('Trapped!')
    else:
        print('Escaped in {} minute(s).'. format(answer))
