import sys
sys.stdin = open('./input/input_1219.txt','r')

def dfs(k):
    global flag
    if k == 99:
        flag = True
        return
    for e in graph[k]:
        if visit[e]:
            continue
        visit[e] = 1
        dfs(e)
        visit[e] = 0
    return

for _ in range(10):
    tc, v = map(int, input().split())
    graph = [[] for _ in range(100)]
    info = list(map(int, input().split()))
    visit = [0] * 100
    for i in range(0, len(info), 2):
        graph[info[i]].append(info[i+1])

    flag = False
    dfs(0)
    if flag:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))