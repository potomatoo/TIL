def permutation(k):
    if k == M:
        print(*order)
    else:
        for i in range(N):
            if len(order) > 0:
                if order[-1] > arr[i]:
                    continue
            order.append(arr[i])
            permutation(k+1)
            order.pop()

N, M = map(int,input().split())
arr = list(map(int,input().split()))
order = []
arr.sort()
permutation(0)