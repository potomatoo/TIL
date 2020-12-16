N = int(input())
nums = list(map(int,input().split()))
start, end = 1, 1
for i in range(len(nums)):
    if nums[i] != i+1:
        start = i
        end = nums[i]
        first = nums[0:start]
        second = nums[start:end-1]
        last = nums[end:-1]
        second.reverse()
        nums = first + second + last
        break
print(start, end)
print(*nums)