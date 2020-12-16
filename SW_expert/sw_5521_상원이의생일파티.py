import sys
sys.stdin = open('./input/input_5521.txt', 'r')
from _collections import deque

TC = int(input())
for tc in range(TC):
    N, M = map(int,input().split())
    friends = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int,input().split())
        friends[a].append(b)
        friends[b].append(a)

    visit = [0] * (N+1)
    v = 1
    Q = deque()
    Q.append((1, 0))
    visit[v] = 1
    ans = 0
    while Q:
        number, dep = Q.popleft()
        if 0 < dep < 3:
            ans += 1
        for w in friends[number]:
            if visit[w]: continue
            Q.append((w, dep+1))
            visit[w] = 1
            number = w

    print('#{} {}'.format(tc+1,ans))
