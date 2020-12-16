from collections import deque

def is_range(k):
    if 0 <= k <= len(visit)-1:
        return True

N, k = map(int,input().split())
visit = [0 for _ in range(100001)]
D = [0 for _ in range(100001)]
Q = deque()
Q.append(N)
visit[N] = 1
while Q:
    find = Q.popleft()
    if find == k:
        break
    multi = find * 2
    plus = find + 1
    minus = find - 1
    if is_range(multi):
        if find != k and visit[multi] == 0:
            Q.append(multi)
            visit[multi] = 1
            D[multi] += D[find] + 1
    if is_range(plus):
        if find != k and visit[plus] == 0:
                Q.append(plus)
                visit[plus] = 1
                D[plus] += D[find] + 1
    if is_range(minus):
        if find != k and visit[minus] == 0:
                Q.append(minus)
                visit[minus] = 1
                D[minus] += D[find] + 1
print(D[k])
