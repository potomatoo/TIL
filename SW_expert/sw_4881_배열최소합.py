import sys
sys.stdin = open('./input/input_4881.txt','r')

def dfs(k):
    global min_result
    global result
    if result > min_result:
        return
    if k == N:
        min_result = min(min_result, result)
        return
    for i in range(N):
        if visit[i]: continue
        result += n_map[k][i]
        visit[i] = 1
        dfs(k+1)
        visit[i] = 0
        result -= n_map[k][i]




TC = int(input())
for tc in range(TC):
    N = int(input())
    n_map = [list(map(int,input().split())) for _ in range(N)]
    visit = [0] * N
    min_result = 0xfffffff
    result = 0
    dfs(0)
    print('#{} {}'.format(tc+1, min_result))