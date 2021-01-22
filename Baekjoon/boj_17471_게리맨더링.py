from itertools import combinations

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
people = [0] + list(map(int, input().split()))
graph = [[] for x in range(N+1)]
parent = [x for x in range(N+1)]
for i in range(1, N+1):
    info = list(map(int, input().split()))
    for j in range(1, len(info)):
        graph[i].append(info[j])
        union_parent(parent, i, info[j])

area = [x for x in range(1, N+1)]

answer = 1e9

for k in range(1, (N//2)+1):
    coms = list(combinations(area, k))

    for com in range(len(coms)):
        A = list(coms[com])
        B = list(set(area) - set(coms[com]))
        parent_flag = True
        find_flag = True
        flag = True
        for i in range(len(A)):
            for j in range(len(A)):
                if i == j:
                    continue

                if parent[A[i]] != parent[A[j]]:
                    parent_flag = False
                    break
            if not parent_flag:
                find_flag = False
                break

        if find_flag:
            for i in range(len(B)):
                for j in range(len(B)):
                    if i == j:
                        continue
                    if parent[B[i]] != parent[B[j]]:
                        parent_flag = False
                        break
                if not parent_flag:
                    find_flag = False
                    break

        if find_flag:
            for i in range(len(A)):
                flagA = False
                for j in range(len(A)):
                    if i == j:
                        continue
                    if A[i] in graph[A[j]]:
                        flagA = True
                        break
                if not flagA:
                    flag = False
                    break

            for i in range(len(B)):
                flagB = False
                for j in range(len(B)):
                    if i == j:
                        continue
                    if B[i] in graph[B[j]]:
                        flagB = True
                        break
                if not flagB:
                    flag = False
                    break

            if flag:
                peopleA = 0
                peopleB = 0
                for a in A:
                    peopleA += people[a]
                for b in B:
                    peopleB += people[b]
                answer = min(answer, abs(peopleA-peopleB))

if answer == 1e9:
    print(-1)
else:
    print(answer)