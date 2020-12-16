import sys
sys.stdin = open('./input/input_5188.txt', 'r')

def dfs(y, x, d):
    global ans
    if d > ans:
        return

    if y == N-1 and x == N-1:
        ans = d
        return

    for i in range(2):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
            continue
        if visit[ty][tx] == 0:
            dfs(ty, tx, d + maze[ty][tx])
            visit[y][x] = 0
    return ans

TC = int(input())

for tc in range(TC):
    N = int(input())
    maze = []
    for _ in range(N):
        maze.append(list(map(int,input().split())))

    dy = [1, 0]
    dx = [0, 1]

    visit = [[0 for _ in range(N)] for _ in range(N)]
    ans = 0xfffff
    print('#{} {}'.format(tc+1, dfs(0, 0, maze[0][0])))
