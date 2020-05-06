from _collections import deque

N, K = map(int,input().split())
Q = deque()
visit = [0] * 100001
Q.append((N, 0))
D = [0] * 100001
while Q:
    find, t = Q.popleft()
    visit[find] = 1
    if find == K:
        print(t)
        result = []
        while t != 0:
            for i in range(len(Q)):
                if Q[i][0] == K:
                    result.append(K)
                            

            break
    if 2*find <= 100000 and visit[2*find] == 0:
        Q.append((2 * find, t+1))

    if find-1 >= 0 and visit[find-1] == 0:
        Q.append((find-1, t+1))

    if find+1 <= 100000 and visit[find+1] == 0:
        Q.append((find+1, t+1))