from _collections import deque

chess = [list(map(str, [*input()])) for _ in range(8)]

dy = [-1, 1, 0, 0, -1, -1, 1, 1, 0]
dx = [0, 0, -1, 1, -1, 1, -1, 1, 0]

wall = []
for y in range(8):
    for x in range(8):
        if chess[y][x] == '#':
            wall.append((y, x))

Q = deque()
check_wall = [0] * 100
check_wall[0] = 1
Q.append((7, 0, 0))
visit = [[[0 for _ in range(100)] for _ in range(8)] for _ in range(8)]

flag = True
while Q:
    y, x, k = Q.popleft()

    if y == 3 or k > 10:
        print(1)
        flag = False
        break

    if not check_wall[k]:
        check_wall[k] = 1
        new_wall = []
        for yy, xx in wall:
            if yy + 1 == 8:
                continue
            new_wall.append((yy + 1, xx))
        for i in range(8):
            for j in range(8):
                chess[i][j] = '.'
                if (i,j) in new_wall:
                    chess[i][j] = '#'
        wall = new_wall

    # if not wall:
    #     print(1)
    #     flag = False
    #     break

    for i in range(9):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > 7 or tx > 7:
            continue
        if chess[ty][tx] == '.':
            if ty > 0:
                if chess[ty-1][tx] != '#':
                    if visit[ty][tx][k] == 0:
                        visit[ty][tx][k] = 1
                        Q.append((ty, tx, k+1))

if flag:
    print(0)