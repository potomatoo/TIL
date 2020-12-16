from collections import deque
def is_range(n):
    if 0 <= n <= N:
        return True

N = int(input())
Q = deque()
visit = [0] * (N+1)
D = [0] * (N+1)
Q.append(N)
visit[N] = 1
cnt = 0
while Q:
    k = Q.popleft()
    if k == 1:
        break
    three = k // 3
    two = k // 2
    one = k - 1
    if is_range(three):
        if k % 3 == 0 and visit[three] == 0:
            visit[three] = 1
            Q.append(three)
            D[three] = D[k] + 1

    if is_range(two):
        if k % 2 == 0 and visit[two] == 0:
            visit[two] = 1
            Q.append(two)
            D[two] = D[k] + 1


    if is_range(one):
        if visit[one] == 0:
            visit[one] = 1
            Q.append(one)
            D[one] = D[k] + 1

print(D[1])

