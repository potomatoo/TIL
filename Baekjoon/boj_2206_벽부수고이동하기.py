from collections import deque
N, M = map(int,input().split())
space = [list(map(int,[*input()])) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
ans = 0xfffffff
Q = deque()
visit = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
Q.append((0, 0, 0, 1))
visit[0][0][0] = 1
while Q:
    yy, xx, p, d = Q.popleft()
    if yy == N-1 and xx == M - 1:
        if ans > d:
            ans = d
        break
    for i in range(4):
        ty = yy + dy[i]
        tx = xx + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
            continue
        if space[ty][tx] == 0 and visit[ty][tx][p] == 0:
            visit[ty][tx][p] = 1
            Q.append((ty, tx, p, d+1))

        elif space[ty][tx] == 1 and p == 0:
            visit[ty][tx][1] = 1
            Q.append((ty, tx, 1, d+1))

if ans == 0xfffffff:
    print(-1)
else:
    print(ans)