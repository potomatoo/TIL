from collections import deque
from sys import stdin

N, M, K = map(int, stdin.readline().split())
space = [list(map(int, stdin.readline().strip())) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
ans = 0xfffffff
Q = deque()
visit = [[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
Q.append((0, 0, 0, 1))
visit[0][0] = [1] * (K+1)
while Q:
    yy, xx, p, d = Q.popleft()

    if yy == N-1 and xx == M - 1:
        if ans > d:
            ans = d
        break
    for i in range(4):
        ty = yy + dy[i]
        tx = xx + dx[i]
        if 0 <= ty < N and 0 <= tx < M and not visit[ty][tx][p]:
            visit[ty][tx][p] = 1
            if not space[ty][tx]:
                Q.append((ty, tx, p, d+1))

            elif p < K:
                visit[ty][tx][p+1] = 1
                Q.append((ty, tx, p+1, d+1))

if ans == 0xfffffff:
    print(-1)
else:
    print(ans)