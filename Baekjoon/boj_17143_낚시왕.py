def fishing(k):
    global answer
    shark.sort(key=lambda x:x[0])
    for si in range(len(shark)):
        if k == shark[si][1]:
            answer += shark[si][4]
            shark.pop(si)
            return

def find_location(y, x, s, d, z):
    origin_s = s
    while s:
        ty = y + dy[d]
        tx = x + dx[d]
        if ty < 0:
            d = 1
            y = 1
        elif ty > R-1:
            d = 0
            y = R-2
        elif tx < 0:
            d = 2
            x = 1
        elif tx > C-1:
            d = 3
            x = C-2
        else:
            y = ty
            x = tx
        s -= 1
    return y, x, origin_s, d, z


def move_shark():
    after_moving = []
    visit = [[0 for _ in range(C)] for _ in range(R)]
    for r, c, s, d, z in shark:
        after_moving.append(find_location(r, c, s, d, z))

    after_moving.sort(key=lambda x: -x[4])
    moving = []
    for ty, tx, s, d, z in after_moving:
        if visit[ty][tx]:
            continue
        visit[ty][tx] = 1
        moving.append((ty, tx, s, d, z))
    return moving

R, C, M = map(int, input().split())
shark = []

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark.append((r-1, c-1, s, d-1, z))

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

answer = 0
for i in range(C):
    fishing(i)
    shark = move_shark()

print(answer)