import sys
sys.stdin = open('input_4615.txt','r')

def isrange(ty, tx):
    if  0 <= ty <= N-1 and 0 <= tx <= N-1:
        return True
    else:
        return False
TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    o_map = [[0 for _ in range(N)] for _ in range(N)]
    dx = [0, 0, -1, 1, 1, -1, -1, 1]
    dy = [1, -1, 0, 0, -1, 1, -1, 1]
    o_map[N//2-1][N//2-1] = o_map[N//2][N//2] = 2
    o_map[N//2][N//2-1] = o_map[N//2-1][N//2] = 1
    for m in range(M):
        x, y, color = map(int,input().split())
        x = x - 1
        y = y - 1
        o_map[y][x] = color
        for i in range(8):
            change_y = []
            change_x = []
            ty = y + dy[i]
            tx = x + dx[i]
            if not isrange(ty,tx):
                continue
            if o_map[ty][tx] == 0 or o_map[ty][tx] == color:
                continue
            while True:
                change_y.append(ty)
                change_x.append(tx)
                ty = ty + dy[i]
                tx = tx + dx[i]
                if not isrange(ty, tx):
                    break
                if o_map[ty][tx] == 0:
                    break

                if o_map[ty][tx] == color:
                    for j in range(len(change_x)):
                        o_map[change_y[j]][change_x[j]] = color
                    break

    x_cnt = 0
    y_cnt = 0
    for y in range(len(o_map)):
        for x in range(len(o_map[y])):
            if o_map[y][x] == 1:
                x_cnt += 1
            if o_map[y][x] == 2:
                y_cnt += 1
    print('#{} {} {}'.format(tc+1,x_cnt,y_cnt))




