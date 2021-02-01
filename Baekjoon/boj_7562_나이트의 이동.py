from collections import deque

TC = int(input())
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]
for tc in range(TC):
    N = int(input())
    start_y = start_x = end_y = end_x = 0
    for i in range(1, 3):
        if i == 1:
            start_y, start_x = map(int, input().split())
        else:
            end_y, end_x = map(int, input().split())

    Q = deque()
    visit = [[0 for _ in range(N)] for _ in range(N)]
    Q.append((start_y, start_x, 1))
    visit[start_y][start_x] = 1

    while Q:
        now_y, now_x, d = Q.popleft()
        if now_y == end_y and now_x == end_x:
            print(d-1)
            break
        for i in range(8):
            ty = now_y + dy[i]
            tx = now_x + dx[i]
            if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                continue
            if not visit[ty][tx]:
                visit[ty][tx] = d+1
                Q.append((ty, tx, d+1))

