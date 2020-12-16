from collections import deque

N = int(input())
maze = [list(map(int,[*input()])) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

flag = True
k = 0
while flag:
    Q = deque()
    visit = [[[0 for _ in range(k+1)] for _ in range(N)] for _ in range(N)]
    Q.append((0, 0, 0))
    visit[0][0][0] = 1
    while Q:
        y, x, p = Q.popleft()
        if y == N-1 and x == N-1:
            print(p)
            flag = False
            break
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                continue
            if maze[ty][tx] == 1 and visit[ty][tx][p] == 0:
                visit[ty][tx][p] = 1
                Q.append((ty, tx, p))

            elif maze[ty][tx] == 0 and p < k:
                visit[ty][tx][1] = 1
                Q.append((ty, tx, p+1))

    k += 1

