from collections import deque

N, M = map(int,input().split())
tomato = []
for _ in range(M):
    tomato.append(list(map(int,input().split())))
visit = [[0 for _ in range(N)]for _ in range(M)]
D = [[0 for _ in range(N)] for _ in range(M)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
Q = deque()
for y in range(len(tomato)):
    for x in range(len(tomato[y])):
        if tomato[y][x] == 1:
            visit[y][x] = 1
            D[y][x] = 1
            Q.append((y,x))
        if tomato[y][x] == -1:
            D[y][x] = -1
while Q:
    y, x = Q.popleft()
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if 0 <= ty < M and 0 <= tx < N and visit[ty][tx] == 0 and tomato[ty][tx] == 0:
            visit[ty][tx] = 1
            Q.append((ty,tx))
            D[ty][tx] += (D[y][x] + 1)

ans = 0
flag = False
for y in range(len(D)):
    for x in range(len(D[y])):
        if D[y][x] == 0:
            flag = True
            print(-1)
            break
        if ans < D[y][x]:
            ans = D[y][x]
    if flag == True:
        break
if flag == False:
    print(ans-1)
