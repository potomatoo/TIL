def get_turn(y,x,d):
    if d == 0:
        tx = x - 1
        return tx
    if d == 1:
        ty = y - 1
        return ty
    if d == 2:
        tx = x + 1
        return tx
    if d == 3:
        ty = y + 1
        return ty

def go_clean(y,x,d):

    if d == 0:
        ty = get_turn(y,x,d)
        if c_map[ty][x] == 0 and visit[ty][x] == 0:
            visit[ty][x] = 1
            go_clean(ty,x,d+3)
        else:
            go_clean(ty, x, d+3)
    if d == 1:
        tx = get_turn(y,x,d)
        if c_map[y][tx] == 0 and visit[y][tx] == 0:
            visit[y][tx] = 1
            go_clean(y,tx,d-1)
        else:
            go_clean(y, tx, d-1)
    if d == 2:
        ty = get_turn(y, x, d)
        if c_map[ty][x] == 0 and visit[ty][x] == 0:
            visit[ty][x] = 1
            go_clean(ty, x, d-1)
        else:
            go_clean(ty, x, d-1)
    if d == 3:
        tx = get_turn(y, x, d)
        if c_map[y][tx] == 0 and visit[y][tx] == 0:
            visit[y][tx] = 1
            go_clean(y, tx, d-1)
        else:
            go_clean(y,tx,d-1)



N, M = map(int,input().split())
r, c, d = map(int,input().split())
c_map = []
for _ in range(N):
    c_map.append(list(map(int,input().split())))
visit = [[0 for _ in range(M)] for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
go_clean(r,c,d)
print(visit)

