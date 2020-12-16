import sys
sys.stdin = open('./input/input_대각_폭탄.txt','r')

def is_range(ty,tx):
    if 0 <= ty <= N-1 and 0 <= tx <= N-1:
        return True
    else:
        return False

TC = int(input())
for tc in range(TC):
    N = int(input())
    b_map = []
    for _ in range(N):
        b_map.append(list(map(int,input().split())))

    dy = [1, 1, -1, -1]
    dx = [-1, 1, 1, -1]
    powers = []
    ys = []
    xs = []
    for y in range(len(b_map)):
        for x in range(len(b_map[y])):
            power = 0
            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]
                if not is_range(ty,tx):
                    continue
                while True:
                    power += b_map[ty][tx]
                    ty = ty + dy[i]
                    tx = tx + dx[i]
                    if not is_range(ty,tx):
                        break
            powers.append(power+b_map[y][x])
            ys.append(y)
            xs.append(x)

    print('#{} {} {} {}'.format(tc+1, ys[powers.index(max(powers))], xs[powers.index(max(powers))], max(powers)))