from collections import deque
def solution(n):
    Q = deque()
    Q.append((0, 0))
    while True:
        now, d = Q.popleft()
        if now == n:
            return d-1
        if now+1 <= n:
            Q.append((now+1, d+1))
        if now*2 <= n:
            Q.appendleft((now*2, d))

print(solution(5))
print(solution(6))
print(solution(5000))