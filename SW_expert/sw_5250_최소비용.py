import sys
sys.stdin = open('./input/input_5250.txt', 'r')
from _collections import deque
TC = int(input())
for tc in range(TC):
    N = int(input())
    area = []
    for _ in range(N):
        area.append(list(map(int,input().split())))


    Q = deque()
    visit = [[0 for _ in range(N)] for _ in range(N)]
    Q.append((0, 0))
    visit[0][0] = 1
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    INF = float('inf')
    D = [[0 for _ in range(N)] for _ in range(N)]

    while Q:
        y, x = Q.popleft()
        if y == N - 1 and x == N - 1:
            print('#{} {}'.format(tc + 1, D[N-1][N-1]))
            break
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                continue

            if not visit[ty][tx]:
                visit[ty][tx] = 1
                D[ty][tx] = D[y][x] + 1 + (area[ty][tx] - area[y][x])
                if area[ty][tx] < area[y][x]:
                    D[ty][tx] = D[y][x] + 1
                Q.append((ty, tx))

            elif visit[ty][tx]:
                new = D[y][x] + 1 + (area[ty][tx] - area[y][x])
                if area[ty][tx] < area[y][x]:
                    new = D[y][x] + 1
                if D[ty][tx] > new:
                    D[ty][tx] = new
                    Q.append((ty, tx))









