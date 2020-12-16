import sys
sys.stdin = open('./input/input_5102.txt', 'r')

from _collections import deque
TC = int(input())
for tc in range(TC):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    visit = [0] * (V+1)
    for i in range(E):
        v, u = map(int, input().split())
        G[v].append(u)
        G[u].append(v)

    start, end = map(int, input().split())
    Q = deque()
    Q.append((start, 0))
    visit[start] = 1
    flag = True
    while Q:
        q, d = Q.popleft()
        if q == end:
            print('#{} {}'.format(tc+1, d))
            flag = False
            break
        for w in G[q]:
            if visit[w] == 1:
                continue
            visit[w] = 1
            Q.append((w, d+1))
    if flag:
        print('#{} {}'.format(tc+1, 0))





