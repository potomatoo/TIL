import sys
sys.setrecursionlimit(100000)

def dfs(y,x):
    visit[y][x] = 1
    cheeze[y][x] = 3
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
            continue
        while cheeze[ty][tx] == 0 and visit[ty][tx] == 0:
            dfs(ty,tx)

def check_c(y,x):
    visit[y][x] = 1
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
            continue
        if cheeze[ty][tx] == 3 and visit[ty][tx] == 0:
            cheeze[y][x] = 0


dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
N, M = map(int,input().split())
cheeze = []
for _ in range(N):
    cheeze.append(list(map(int,input().split())))

cnt = 0
while True:
    cnt += 1
    # 테두리에서 dfs로 빈 공간을 3으로 바꿔준다.
    visit = [[0 for _ in range(M)] for _ in range(N)]
    dfs(0,0)

    last_cheeze = 0
    for y in range(N):
        for x in range(M):
            if cheeze[y][x] == 1:
                last_cheeze += 1


    # 치즈의 녹을 수 있는 부분을 녹여준다.
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if cheeze[y][x] == 1:
                check_c(y,x)

    check_last = 0
    for y in range(N):
        for x in range(M):
            if cheeze[y][x] == 3:
                cheeze[y][x] = 0
            if cheeze[y][x] == 1:
                check_last += 1

    if check_last == 0:
        print(cnt)
        print(last_cheeze)
        break











