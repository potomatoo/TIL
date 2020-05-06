n, m = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))
dp = [[0] * (m + 1) for _ in range(n + 1)]

for y in range(1, n + 1):
    for x in range(1, m + 1):
        dp[y][x] = room[y - 1][x - 1] + max(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1])
print(dp[n][m])