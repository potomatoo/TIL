import sys
sys.stdin = open('./input/input_1861.txt','r')
sys.setrecursionlimit(1000000)
def dfs(y,x):
    global long
    visit[y][x] = 1
    long += 1
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
            continue
        if b_map[ty][tx] == b_map[y][x] + 1:
            dfs(ty,tx)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
TC = int(input())
for tc in range(TC):
    N = int(input())
    b_map = []
    for _ in range(N):
        b_map.append(list(map(int,input().split())))
    visit = [[0 for _ in range(N)]for _ in range(N)]
    max_long = -0xfffffff
    num = -0xffffffff
    for y in range(N):
        for x in range(N):
            long = 0
            dfs(y,x)
            if long >= max_long:
                if long == max_long and (b_map[y][x] > num):
                    max_long = long

                else:
                    max_long = long
                    num = b_map[y][x]
    print('#{} {} {}'.format(tc+1, num, max_long))