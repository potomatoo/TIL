from _collections import deque
V, E, P = map(int,input().split())
G = [[] for _ in range(V+1)]
pay = []
for _ in range(E):
    a, b, c = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
    pay.append([a, b, c])
    pay.append([b, a, c])
Q = deque()
Q.append(1)