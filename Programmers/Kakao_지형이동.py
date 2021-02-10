dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def solution(land, height):
    global dy, dx
    N = len(land)
    visit = [[0] * N for _ in range(N)]
    line = []
    one = []
    def dfs(y, x, check):
        global dy, dx
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or ty > N - 1 or tx < 0 or tx > N - 1:
                continue
            if not visit[ty][tx] and abs(land[y][x] - land[ty][tx]) <= height:
                visit[ty][tx] = check
                dfs(ty, tx, check)
    cnt = 1
    for y in range(N):
        for x in range(N):
            if visit[y][x] == 0:
                dfs(y, x, cnt)
                cnt += 1

    visit2 = [[0] * N for _ in range(N)]
    line = []
    result = dict()
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]
                if ty < 0 or ty > N-1 or tx < 0 or tx > N-1:
                    continue
                if not visit2[ty][tx] and visit[y][x] != visit[ty][tx]:
                    visit2[y][x] = 1
                    visit2[ty][tx] = 1
                    a = min(visit[y][x], visit[ty][tx])
                    b = max(visit[y][x], visit[ty][tx])
                    if '{} {}'.format(a, b) in result:
                        result['{} {}'.format(a, b)] = min(result['{} {}'.format(a, b)], (abs(land[y][x] - land[ty][tx])))
                    else:
                        result['{} {}'.format(a, b)] = abs(land[y][x] - land[ty][tx])

                    line.append([land[y][x], land[ty][tx], visit[y][x], visit[ty][tx]])

    result_value = list(result.values())
    result_value.sort()

    answer = sum(result_value[:cnt-2])

    return answer

print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))
