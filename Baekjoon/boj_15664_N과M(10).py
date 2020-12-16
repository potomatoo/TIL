def pemutation(k):
    if k == M:
        print(*order)
    else:
        before = -1
        for i in range(N):
            if visit[i] == 1 or before == nums[i]:
                continue
            if len(order) > 0:
                if order[-1] > nums[i]:
                    continue
            visit[i] = 1
            before = nums[i]
            order.append(nums[i])
            pemutation(k+1)
            visit[i] = 0
            order.pop()


N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
visit = [0] * N
order = []
pemutation(0)
