import sys
sys.stdin = open('./input/input_1865.txt','r')

def dfs(k):
    global max_ans
    global ans

    if k == N:
        max_ans = max(ans, max_ans)
        return
    else:
        for i in range(N):
            if visit[i] == 1:
                continue
            if w_map[k][i] == 0:
                continue
            visit[i] = 1
            ans *= (w_map[k][i]/100)
            dfs(k+1)
            visit[i] = 0
            ans /= (w_map[k][i]/100)

TC = int(input())
for tc in range(TC):
    N = int(input())
    w_map = []
    for _ in range(N):
        w_map.append(list(map(int,input().split())))
    max_ans = 0
    ans = 0
    visit = [0 for _ in range(N)]
    dfs(0)
    print(max_ans)