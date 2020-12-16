def permutation(k, n):
    global cnt
    if k == n:
        if len(set(order)) == len(order):
            cnt += 1
    else:
        before = -1
        for i in range(len(arr)):
            if visit[i] or arr[i] == before:
                continue
            if len(order) > 0:
                if i != arr.index(order[-1]) + 1:
                    continue
            before = arr[i]
            visit[i] = 1
            order.append(arr[i])
            permutation(k+1, n)
            visit[i] = 0
            order.pop()


N = int(input())
arr = list(map(int, input().split()))
cnt = 0
order = []
visit = [0] * N
ans = set()
for leng in range(1, N+1):
    permutation(0, leng)
print(cnt)
