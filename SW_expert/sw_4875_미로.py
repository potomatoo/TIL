import sys
sys.stdin = open('./input/input_4875.txt','r')

def dfs(y,x):
    if maze[y][x] == '3':
        return 1

    visit[y][x] = 1
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
            continue
        while (maze[ty][tx] == '0' or maze[ty][tx] == '3') and visit[ty][tx] == 0:
            if backtrack(ty,tx):
                return 1

    else:
        return 0

TC = int(input())
for tc in range(TC):
    N = int(input())
    maze = []
    visit = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(N):
        maze.append(input())
    start_y = 0
    start_x = 0

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == '2':
                start_y = y
                start_x = x

    print('#{} {}'.format(tc+1, dfs(start_y, start_x)))