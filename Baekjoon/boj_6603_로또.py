def permutation(k,s):
    global sum_
    if k == 6:
        print(*order)
    else:
        for i in range(s,N):
            if visit[i] == 1:
                continue
            visit[i] = 1
            order.append(nums[i])
            permutation(k+1,i+1)
            visit[i] = 0
            order.pop()

while True:
    input_ = list(map(int,input().split()))
    if input_ == [0]:
        break
    N = input_[0]
    nums = input_[1:]
    visit = [0] * N
    order = []
    permutation(0,0)
    print()