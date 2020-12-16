import sys
sys.stdin = open('./input/input_1249.txt', 'r')
from _collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
TC = int(input())
for tc in range(TC):
    N = int(input())
    ground = []
    for _ in range(N):
        ground.append(list(map(int,[*input()])))
    INF = float('INF')
    D = [[INF for _ in range(N)] for _ in range(N)]
    D[0][0] = 0
    ans = 0xfffffff
    Q = deque()
    Q.append((0, 0))

    while Q:
        y, x = Q.popleft()
        if D[y][x] > ans:
            continue
        if y == N-1 and x == N-1:
            ans = D[N-1][N-1]
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                continue
            if D[y][x] + ground[ty][tx] < D[ty][tx]:
                Q.append((ty, tx))
                D[ty][tx] = D[y][x] + ground[ty][tx]
    print('#{} {}'.format(tc+1, ans))
