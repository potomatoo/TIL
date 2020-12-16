from _collections import deque

K = int(input())
M, N = map(int,input().split())

space = []
for _ in range(N):
    space.append(list(map(int,input().split())))

dy = [-1, 1, 0, 0, -1, -2, -2, -1, 1, 2, 2, 1]
dx = [0, 0, -1, 1, -2, -1, 1, 2, 2, 1, -1, -2]

Q = deque()
visit = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
Q.append((0, 0, 0))
flag = True
while Q:
    y, x, p = Q.popleft()
    if p == K:
        j = 4
    else:
        j = 12

    if y == N-1 and x == M-1:
        print(visit[y][x][p])
        flag = False
        break

    for i in range(j):
        ty = y + dy[i]
        tx = x + dx[i]
        if i < 4:
            tp = p
        else:
            tp = p + 1
        if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
            continue
        if not visit[ty][tx][tp] and not space[ty][tx]:
            visit[ty][tx][tp] = visit[y][x][p] + 1
            Q.append((ty, tx, tp))

if flag:
    print(-1)