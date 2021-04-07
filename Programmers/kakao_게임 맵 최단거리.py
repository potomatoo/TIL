from collections import deque

def bfs(N, M, maps):
    global answer, flag
    Q = deque()
    Q.append((0, 0, 1))
    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit[0][0] = 1
    while Q:
        y, x, d = Q.popleft()
        if y == N-1 and x == M-1:
            answer = d
            return True
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
                continue
            if maps[ty][tx] and not visit[ty][tx]:
                visit[ty][tx] = 1
                Q.append((ty, tx, d+1))
    return False

dy = [-1, 1, 0, 0]
dx = [0, 0, -1 ,1]
answer = 0

def solution(maps):
    global answer
    N = len(maps)
    M = len(maps[0])
    if bfs(N, M, maps):
        return answer
    else:
        return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))