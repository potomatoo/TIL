import sys
sys.setrecursionlimit(1000000)

def dfs(y,x,cnt):
    visit[y][x] = 1
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > h-1 or tx > w-1:
            continue
        while b_map[ty][tx] == 1 and visit[ty][tx] == 0:
            dfs(ty,tx,cnt)

TC = int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for tc in range(TC):
    w,h,n = map(int,input().split())
    b_map = [[0 for _ in range(w)] for _ in range(h)]
    visit = [[0 for _ in range(w)] for _ in range(h)]
    for _ in range(n):
        x, y = map(int,input().split())
        b_map[y][x] = 1
    cnt = 0
    for y in range(h):
        for x in range(w):
            if b_map[y][x] == 1 and visit[y][x] == 0:
                cnt += 1
                dfs(y,x,cnt)
    print(cnt)