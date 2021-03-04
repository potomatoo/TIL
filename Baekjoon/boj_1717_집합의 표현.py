import sys
sys.setrecursionlimit(10**5)


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(v1, v2):
    v1 = find_parent(v1)
    v2 = find_parent(v2)
    if v1 < v2:
        parent[v2] = v1
    else:
        parent[v1] = v2

n, m = map(int, input().split())
parent = [x for x in range(n+1)]

for _ in range(m):
    t, a, b = map(int, input().split())
    if t == 0:
        union_parent(a, b)
    elif t == 1:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')