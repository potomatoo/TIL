import sys
sys.stdin = open('./input/input_5105.txt', 'r')
from _collections import deque

TC = int(input())
for tc in range(TC):
    N = int(input())
    maze = [list(map(int, [*input()])) for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    Q = deque()
    visit = [[0 for _ in range(N)] for _ in range(N)]
    flag = True
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 3:
                Q.append((y, x, -1))
                visit[y][x] = 1
                while Q:
                    yy, xx, d = Q.popleft()
                    if maze[yy][xx] == 2:
                        print('#{} {}'.format(tc+1, d))
                        flag = False
                        break
                    for i in range(4):
                        ty = yy + dy[i]
                        tx = xx + dx[i]
                        if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                            continue
                        if (maze[ty][tx] == 0 or maze[ty][tx] == 2) and visit[ty][tx] == 0:
                            visit[yy][xx] = 1
                            Q.append((ty, tx, d+1))
    if flag:
        print('#{} {}'.format(tc+1, 0))



