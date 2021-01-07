from collections import deque

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]
def solution(board):
    answer = []
    N = len(board)
    def bfs(start_y, start_x, start_cost, start_d):
        Q = deque()
        Q.append((start_y, start_x, start_cost, start_d))
        visit = [[0 for _ in range(N)] for _ in range(N)]
        while Q:
            y, x, cost, d = Q.popleft()
            new_cost = 0
            if y == N-1 and x == N-1:
                answer.append(cost)
            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]
                if ty < 0 or ty > N-1 or tx < 0 or tx > N-1:
                    continue
                if d == i:
                    new_cost = cost + 100
                else:
                    new_cost = cost + 600
                if not board[ty][tx]:
                    if not visit[ty][tx] or visit[ty][tx] > new_cost:
                        visit[ty][tx] = new_cost
                        Q.append((ty, tx, new_cost, i))

    bfs(0, 0, 0, 0)
    bfs(0, 0, 0, 1)
    return min(answer)

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))