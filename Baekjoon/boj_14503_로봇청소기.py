n, m = map(int, input().split())
x, y, d = map(int, input().split())
c_map = [list(map(int, input().split())) for _ in range(n)]
c_map[x][y] = 2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def solve(x, y, d, cnt):
    while True:
        c = False
        for k in range(4):
            nd = (d+3) % 4
            tx = x + dx[nd]
            ty = y+dy[nd]
            d = nd
            if c_map[tx][ty] == 0:
                c_map[tx][ty] = 2
                cnt += 1
                x = tx
                y = ty
                c = True
                break
        if c == False:
            if c_map[x-dx[d]][y-dy[d]] == 1:
                return cnt
            else:
                x = x - dx[d]
                y = y - dy[d]

print(solve(x, y, d, 1))


