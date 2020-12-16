from _collections import deque

N = int(input())
M = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
check = list(map(int,input().split()))

G = [[] for _ in range(N+1)]

for y in range(N):
    for x in range(N):
        if arr[y][x] == 1:
            G[y+1].append(x+1)

visit = [0] * (N+1)
v = check[0]
Q = deque()
Q.append(v)
visit[v] = 1
while Q:
    v = Q.popleft()
    for e in G[v]:
        if visit[e]: continue
        visit[e] = 1
        Q.append(e)

        v = e

flag = True

for i in check:
    if visit[i] == 0:
        print('NO')
        flag = False
        break
if flag:
    print('YES')
