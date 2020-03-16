def dfs(y,x,cnt):
    global ans
    if order.count('Y') >= 4:
        return
    if cnt == 6:
        # print(order)
        # print(seven_princess)
        ans += 1
        return

    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or tx < 0 or ty > 4 or tx > 4:
            continue
        if visit[ty][tx] == 0:
            visit[ty][tx] = 1
            seven_princess.append(sit_nums[ty][tx])
            order.append(sit[ty][tx])
            dfs(ty,tx,cnt+1)
            seven_princess.pop()
            order.pop()
            visit[ty][tx] = 0

sit = []
for y in range(5):
    sit.append(input())

sit_nums = []
k = 1
for _ in range(5):
    sit_nums.append([x for x in range(k,k+5)])
    k += 5

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
ans = 0
for y in range(5):
    for x in range(5):
        visit = [[0 for _ in range(5)] for _ in range(5)]
        seven_princess = [sit_nums[y][x]]
        order = [sit[y][x]]
        visit[y][x] = 1
        dfs(y, x, 0)
print(ans)


