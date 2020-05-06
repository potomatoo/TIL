import sys
sys.stdin = open('./input/input_test.txt', 'r')

def dfs(y, x):
    visit[y][x] = 1
    for i in range(8):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > 9 or tx > 9:
            continue
        while sky[ty][tx] == 1 and visit[ty][tx] == 0:
            dfs(ty, tx)

dy = [-1, 1, 0, 0, 1, -1, 1, -1]
dx = [0, 0, -1, 1, 1, -1, -1, 1]

TC = int(input())
for tc in range(TC):
    sky = []
    for _ in range(10):
        sky.append(list(map(int,input().split())))

    visit = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0
    for y in range(10):
        for x in range(10):
            if sky[y][x] == 1 and visit[y][x] == 0:
                cnt += 1
                dfs(y, x)
    print('#{} {}'.format(tc+1, cnt))
    