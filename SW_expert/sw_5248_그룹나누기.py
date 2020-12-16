import sys
sys.stdin = open('./input/input_5248.txt', 'r')
from _collections import deque

TC = int(input())
for tc in range(TC):
    N, M = map(int,input().split())
    G = [[] for _ in range(N+1)]
    arr = list(map(int,input().split()))
    for i in range(0, len(arr), 2):
        G[arr[i]].append(arr[i+1])
        G[arr[i+1]].append(arr[i])

    visit = [0] * (N+1)
    cnt = 0
    for i in range(1,N+1):
        if not visit[i]:
            cnt += 1
            Q = deque()
            Q.append(i)
            visit[i] = 1
            while Q:
                a = 1
                v = Q.popleft()
                for e in G[v]:
                    if visit[e]: continue
                    visit[e] = 1
                    Q.append(e)

    print('#{} {}'.format(tc+1,cnt))



