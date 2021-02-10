
visit = [0 for _ in range(201)]

def solution(n, computers):
    def dfs(y):
        for x in range(n):
            if visit[x]: continue
            if computers[y][x] == 1:
                visit[x] = 1
                dfs(x)
    count = 0
    for y in range(n):
        for x in range(n):
            if visit[x]: continue
            if computers[y][x] == 1:
                visit[x] = 1
                dfs(y)
                count += 1
    return count

print(solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]))