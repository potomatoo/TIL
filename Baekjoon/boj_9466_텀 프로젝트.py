import sys
sys.setrecursionlimit(10**5)

def dfs(idx, n):
    global flag
    if idx == n:
        flag = False
        visit[n] = 1
        return
    elif visit[idx]:
        flag = False
        return
    elif n in path:
        return
    path.append(n)
    dfs(n, board[n])

TC = int(input())
for _ in range(TC):
    N = int(input())
    board = [0] + list(map(int, input().split()))
    visit = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        if visit[i]: continue
        if i == board[i]:
            visit[i] = 1
            continue
        flag = True
        path = []
        dfs(i, board[i])
        if flag:
            if i in path:
                for j in range(len(path)):
                    visit[path[j]] = 1
            else:
                visit[i] = 2
        else:
            visit[i] = 2
    print(visit[1:].count(2))
