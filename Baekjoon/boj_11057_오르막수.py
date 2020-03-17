N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N)]
dp[0] = [1 for _ in range(10)]
for i in range(1,N):
    for j in range(10):
        for k in range(j,10):
            dp[i][k] += dp[i-1][j]

print(sum(dp[-1]) % 10007)
