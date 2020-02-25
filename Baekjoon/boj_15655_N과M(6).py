def permutation(k):
    if k == M:
        print(*order)
    else:
        for i in range(N):
            if visit[i] == 1:
                continue
            if len(order) > 0:
                if order[-1] > arr[i]:
                    continue
            visit[i] = 1
            order.append(arr[i])
            permutation(k+1)
            visit[i] = 0
            order.pop()

N, M = map(int,input().split())
arr = list(map(int,input().split()))
n = len(arr)
visit = [0] * n
order = []
arr.sort()
permutation(0)