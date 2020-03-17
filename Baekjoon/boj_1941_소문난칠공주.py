def dfs(k):
    global ans

    if k == 7:
        print(order)
        print(force)
    else:
        for y in range(5):
            for x in range(5):
                if visit[y][x] == 1: continue
                visit[y][x] = 1
                order.append(sit[y][x])
                force.append(school[y][x])
                dfs(k+1)
                visit[y][x] = 0
                order.pop()
                force.pop()

school = []
for y in range(5):
    school.append(input())

sit = []
k = 1
for _ in range(5):
    sit.append([x for x in range(k, k+5)])
    k += 5
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visit = [[0 for _ in range(5)] for _ in range(5)]
order = []
force = []
dfs(0)
