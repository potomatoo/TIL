def solution(n):
    ans = 0
    while n:
        ans += (n % 2)
        n //= 2
    return ans
print(solution(5000))


'''
- bfs 시간초과 코드

from _collections import deque

def solution(n):
    def bfs():
        Q = deque()
        visit = [0] * (n+1)
        Q.append((0, 0))
        while Q:
            now, cost = Q.popleft()
            if now == n:
                return cost
            if now > n:
                continue
            if not visit[now]:
                visit[now] = 1
                Q.append((now * 2, cost))
                Q.append((now+1, cost+1))

    ans = bfs()
    return ans
'''