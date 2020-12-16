import sys
sys.stdin = open('./input/input_1949.txt','r')

def dfs(y,x,cnt):
    global long
    if cnt > long:
        long = cnt
    visit[y][x] = 1
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
            continue
        if hiking[ty][tx] >= hiking[y][x]:
            continue
        if hiking[ty][tx] < hiking[y][x] and visit[ty][tx] == 0:
            dfs(ty,tx,cnt+1)
            visit[ty][tx] = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

TC = int(input())
for tc in range(TC):
    N, k = map(int,input().split())
    hiking = []
    for _ in range(N):
        hiking.append(list(map(int,input().split())))

    top = []
    max_top = 0
    for y in range(N):
        for x in range(N):
            if hiking[y][x] >= max_top:
                max_top = hiking[y][x]

    for y in range(N):
        for x in range(N):
            if max_top == hiking[y][x]:
                top.append((y,x))


    max_long = 0
    for i in range(N):
        for j in range(N):
            for t in range(k+1):
                for y, x in top:
                    hiking[i][j] = hiking[i][j] - t
                    long = 0
                    visit = [[0 for _ in range(N)] for _ in range(N)]
                    dfs(y,x,1)
                    hiking[i][j] = hiking[i][j] + t
                    if long > max_long:
                        max_long = long

    print('#{} {}'.format(tc+1,max_long))




