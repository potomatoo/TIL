def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
parent = [x for x in range(N+1)]
node = []
for _ in range(M):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

for i in range(1, N+1):
    find_parent(parent, i)

check = []
answer = [0] * (N+1)
for i in range(len(cost)):
    if parent[i] not in check:
        check.append(parent[i])
        answer[parent[i]] = cost[i]
    else:
        mid_check = min(answer[parent[i]], cost[i])
        answer[parent[i]] = mid_check

if k >= sum(answer):
    print(sum(answer))
else:
    print('Oh no')