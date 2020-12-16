def pemutation(k):
    if k == M:
        print(*order)
    else:
        before = -1
        for i in range(N):
            if before == nums[i]:
                continue
            before = nums[i]
            order.append(nums[i])
            pemutation(k+1)
            order.pop()


N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
order = []
pemutation(0)