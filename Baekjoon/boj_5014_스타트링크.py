from collections import deque

def is_range(k):
    if 0 < k <= F:
        return True

F, S, G, U, D = map(int,input().split())

Q = deque()
visit = [0] * (F+1)
route = [0] * (F+1)
Q.append(S)
visit[S] = 1

while Q:
    find = Q.popleft()
    if find == G:
        break

    up = find + U
    down = find - D

    if is_range(up):
        if find != G and visit[up] == 0:
            Q.append(up)
            visit[up] = 1
            route[up] += route[find] + 1

    if is_range(down):
        if find != G and visit[down] == 0:
            Q.append(down)
            visit[down] = 1
            route[down] += route[find] + 1

if S == G:
    print(0)

elif route[G] == 0:
    print('use the stairs')
else:
    print(route[G])



