import sys
sys.stdin = open('./input/input_1226.txt','r')

def dfs(y,x):
    if maze[y][x] == '3':
        return 1
    visit[y][x] = 1
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        while visit[ty][tx] == 0 and (maze[ty][tx] == '0' or maze[ty][tx] == '3'):
            if dfs(ty,tx):
                return 1
    return 0


for tc in range(10):
    n = int(input())
    maze = []
    for _ in range(16):
        maze.append(input())


    visit = [[0 for _ in range(16)] for _ in range(16)]
    S= []
    dy = [0,-1,0,1]
    dx = [1,0,-1,0]
    start = [0,0]
    end = [0,0]
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == '2':
                start = [y,x]
            if maze[y][x] == '3':
                end = [y,x]

    y, x = start[0], start[1]
    print('#{} {}'.format(n,dfs(y,x)))

