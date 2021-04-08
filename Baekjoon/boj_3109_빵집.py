def dfs(y, x):
    global answer, flag
    if x == M-1 and not flag:
        answer += 1
        flag = True
        return

    if flag:
        return
    else:
        for i in range(3):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
                continue
            if not visit[ty][tx] and board[ty][tx] == '.':
                visit[ty][tx] = 1
                dfs(ty, tx)
                if flag:
                    return
                # visit[ty][tx] = 0

dy = [-1, 0, 1]
dx = [1, 1, 1]
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

answer = 0
visit = [[0 for _ in range(M)] for _ in range(N)]
for k in range(N):
    flag = False
    dfs(k, 0)

print(answer)