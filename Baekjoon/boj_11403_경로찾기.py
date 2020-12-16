N = int(input())
G = [[] for _ in range(N)]
S = []
for j in range(N):
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if a[i] == 1:
            G[j].append(i)

result = [[0 for _ in range(N)]for _ in range(N)]
for k in range(N):
    cnt = 0
    visit = [0] * N
    v = k
    S.append(v)
    while S:
        for w in G[v]:
            if visit[w] == 1:
                continue
            S.append(v)
            visit[w] = 1
            result[k][w] = 1
            v = w
            break
        else:
            v = S.pop()

for y in range(len(result)):
    print(*result[y])




