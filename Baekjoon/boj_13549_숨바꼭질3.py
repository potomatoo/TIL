from _collections import deque

N, K = map(int,input().split())
Q = deque()
visit = [0] * 100001
Q.append((N, 0))


while Q:
    find, t = Q.popleft()
    if find == K:
        print(t)
        break
    if 2*find <= 100000 and visit[2*find] == 0:
        Q.append((2 * find, t))
        visit[2 * find] = 1

    if find-1 >= 0 and visit[find-1] == 0:
        Q.append((find - 1, t + 1))
        visit[find - 1] = 1

    if find+1 <= 100000 and visit[find+1] == 0:
        Q.append((find+1, t+1))
        visit[find+1] = 1