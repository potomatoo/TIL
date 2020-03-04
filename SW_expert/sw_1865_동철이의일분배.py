import sys
sys.stdin = open('./input/input_1865.txt','r')

def dfs(k, ans):
    global max_ans
    if ans <= max_ans:
        return
    if k == N:
        max_ans = max(max_ans, ans)
        return
    for i in range(N):
        if visit[i] == 1:
            continue
        visit[i] = 1
        dfs(k+1, ans * w_map[k][i])
        visit[i] = 0


TC = int(input())
for tc in range(TC):
    N = int(input())
    w_map = []
    for _ in range(N):
        w_map.append(list(map(int,input().split())))
    for y in range(N):
        for x in range(N):
            w_map[y][x] = w_map[y][x] / 100
    max_ans = 0
    visit = [0 for _ in range(N)]
    dfs(0, 1)
    print('#{} {:.6f}'.format(tc+1, max_ans * 100))