def go_shark(r, c, s, d, z, v):
    if d == 1:
        ty = r - 1
        tx = c
        if ty < 0:
            go_shark(r, c, )

def eat_shark():
    for y in range(R):
        for x in range(C):
            if len(sea[y][x]) > 1:
                sea[y][x] = max(sea[y][x], key=lambda item:item[2])


R, C, S = map(int,input().split())
sea = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(S):
    r, c, s, d, z = map(int, input().split())
    r = r - 1
    c = c - 1
    sea[r][c].append([s, d, z, 0])

for i in range(C):
    for j in range(R):
        if len(sea[j][i]) != 0:
            sea[j][i] = []
            for y in range(R):
                for x in range(C):
                    if len(sea[y][x]) > 0:
                        for s, d, z, v in sea[y][x]:
                            if v == 0:
                                go_shark(y, x, s, d, z, v)


ans = 0
print(ans)