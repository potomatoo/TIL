from itertools import combinations

def dfs(k, com):
    for v in graph[k]:
        if visit[v]:
            continue
        visit[v] = 1
        if v in com:
            dfs(v, com)

N = int(input())
people = [0] + list(map(int, input().split()))
graph = []

for i in range(1, N+1):
    info = list(map(int, input().split()))
    graph.append(info[1:])

graph = [[]] + graph
area = [x for x in range(1, N+1)]
answer = 1e9

for k in range(1, N):
    com = list(combinations(area, k))
    for A in com:
        A = list(A)
        B = list(set(area) - set(A))
        if len(A) + len(B) != N:
            continue
        flag = True
        if len(A) > 1:
            visit = [0] * (N+1)
            dfs(A[0], A)
            for a in A:
                if not visit[a]:
                    flag = False

        if len(B) > 1 and flag:
            visit = [0] * (N + 1)
            dfs(B[0], B)
            for b in B:
                if not visit[b]:
                    flag = False

        if flag:
            people_A = 0
            people_B = 0
            for a in A:
                people_A += people[a]
            for b in B:
                people_B += people[b]
            if abs(people_B - people_A) < answer:
                result_b = B
                result_a = A
                answer = min(answer, abs(people_B-people_A))

if answer == 1e9:
    print(-1)
else:
    print(answer)
