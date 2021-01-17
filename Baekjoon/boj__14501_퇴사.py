def dfs(k, cost):
    global answer
    if k > N:
        return
    if k + days[k] > N + 1:
        answer = max(answer, cost - costs[k])
    else:
        answer = max(answer, cost)
    for i in graph[k]:
        if visit[i]:
            continue
        visit[i] = 1
        dfs(i, cost + costs[i])
        visit[i] = 0

answer = 0
N = int(input())
graph = [[] for _ in range(N+1)]
costs = [0] * (N+1)
visit = [0] * (N+1)
days = [0] * (N+1)
for i in range(N):
    day, cost = map(int, input().split())
    costs[i+1] = cost
    days[i+1] = day
    if i+day+1 > N:
        continue
    for j in range(i+day+1, N+1):
        graph[i+1].append(j)
for i in range(1, N+1):
    visit = [0] * (N + 1)
    dfs(i, costs[i])

print(answer)




