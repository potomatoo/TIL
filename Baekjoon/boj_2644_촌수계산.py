def dfs(board, v, visit, cnt):
    global flag
    visit[v] = 1
    if v == b:
        flag = cnt
        return
    for i in board[v]:
        if not visit[i]:
            visit[i] = 1
            dfs(board, i, visit, cnt+1)

N = int(input())
a, b = map(int, input().split())
k = int(input())
board = [[] for _ in range(N+1)]
visit = [0] * (N+1)
flag = 0

for _ in range(k):
    parent, child = map(int, input().split())
    board[parent].append(child)
    board[child].append(parent)

dfs(board, a, visit, 0)
if flag:
    print(flag)
else:
    print(-1)






