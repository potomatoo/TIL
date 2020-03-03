from collections import deque
N, M = map(int, input().split())
miro = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
D = [[0] * M for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
Q = deque()
visited[0][0] = 1
D[0][0] = 1
Q.append((0, 0))
while Q:
    x, y = Q.popleft()
    for d in range(4):
        tx, ty = x + dx[d], y + dy[d]
        if 0 <= tx < N and 0 <= ty < M and miro[tx][ty] and not visited[tx][ty]:
            visited[tx][ty] = 1
            Q.append((tx, ty))
            D[tx][ty] = D[x][y] + 1

print(D[N-1][M-1])
