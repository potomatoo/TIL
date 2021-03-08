from collections import deque

def bfs(start_y, start_x, start_d):
    Q = deque()
    visit = [[[0, 0, 0, 0] for _ in range(M)] for _ in range(N)]
    Q.append((start_y, start_x, start_d, 0))
    visit[start_y][start_x][start_d] = 1
    while Q:
        now_y, now_x, now_d, cnt = Q.popleft()
        if now_y == end_y and now_x == end_x and now_d == end_d:
            return cnt
        ty, tx = now_y, now_x
        for _ in range(3):
            ty += dy[now_d]
            tx += dx[now_d]
            if 0 <= ty < N and 0 <= tx < M and visit[ty][tx][now_d] == 1: continue
            if 0 <= ty < N and 0 <= tx < M and not board[ty][tx]:
                visit[ty][tx][now_d] = 1
                Q.append((ty, tx, now_d, cnt + 1))
            else:
                break
        for i in range(4):
            if now_d != i and not visit[now_y][now_x][i]:
                visit[now_y][now_x][i] = 1
                if (now_d == 0 and i == 1) or (now_d == 1 and i == 0) or (now_d == 2 and i == 3) or (now_d == 3 and i == 2):
                    Q.append((now_y, now_x, i, cnt + 2))
                else:
                    Q.append((now_y, now_x, i, cnt + 1))

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
start_y, start_x, start_d = map(int, input().split())
start_y, start_x = start_y-1, start_x-1
end_y, end_x, end_d = map(int, input().split())
end_y, end_x = end_y-1, end_x-1
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

print(bfs(start_y, start_x, start_d))



