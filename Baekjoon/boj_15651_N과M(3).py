def permutation(k):
    if k == M:
        print(*order)
    else:
        for i in range(N):
            order.append(arr[i])
            permutation(k+1)
            order.pop()



N, M = map(int,input().split())
arr = [x for x in range(1,N+1)]
n = len(arr)

order = []
permutation(0)