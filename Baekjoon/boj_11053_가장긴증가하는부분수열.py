N = int(input())
nums = list(map(int,input().split()))
dp = [0] * 1001
dp[0] = 1

for i in range(1,len(nums)):
    if nums[i] > nums[i-1]:
        dp[i] = 1

print(dp.count(1))