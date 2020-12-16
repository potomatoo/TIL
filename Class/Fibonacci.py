# Recursive
memo = [0] * 100
def fibo_memo(n):
    if n <= 2:
        return 1
    if memo[n] == 0:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)

# DP
def fibo_iter(n):
    dp = [0] * 100
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[i]

print(fibo_iter(10))
