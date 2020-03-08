from copy import deepcopy

def permutation(k):
    if k == M:
        c_order = deepcopy(order)
        chicken.append(c_order)
    else:
        for i in range(len(w_chicken)):
            if visit[i] == 1: continue
            if len(order) > 0:
                if order[-1] > w_chicken[i]:
                    continue
            visit[i] = 1
            order.append(w_chicken[i])
            permutation(k+1)
            visit[i] = 0
            order.pop()

N, M = map(int,input().split())
street = []
for _ in range(N):
    street.append(list(map(int,input().split())))

w_chicken = []
for y in range(N):
    for x in range(N):
        if street[y][x] == 2:
            w_chicken.append((y,x))

visit = [0 for _ in range(len(w_chicken))]
order = []
chicken = []
permutation(0)

min_distance = 0xffffff
for k in range(len(chicken)):
    sum_distance = 0
    for yy in range(N):
        for xx in range(N):
            if street[yy][xx] == 1:
                distance = 0xfffff
                for y, x in chicken[k]:
                    distance2 = abs(yy - y) + abs(xx - x)
                    if distance > distance2:
                        distance = distance2
                sum_distance += distance
    if min_distance > sum_distance:
        min_distance = sum_distance

print(min_distance)