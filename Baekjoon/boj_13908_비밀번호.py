def permutation(k):
    global cnt
    visit = [0] * 10
    if k == n:
        for j in range(n):
            visit[order[j]] = 1
        flag = True
        for check in know:
            if not visit[check]:
                flag = False
                break

        if flag:
            cnt += 1
    else:
        for i in range(len(arr)):
            order.append(arr[i])
            permutation(k+1)
            order.pop()

n, m = map(int,input().split())
know = list(map(int,input().split()))
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
order = []
cnt = 0
permutation(0)
print(cnt)