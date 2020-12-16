import sys
sys.stdin = open('./input/input_폭격작전_01.txt','r')

TC = int(input())
for tc in range(TC):
    N, M = map(int,input().split())
    b_map = []
    for _ in range(N):
        b_map.append(list(map(int,input().split())))
    powers = []
    ys = []
    xs = []
    for r in range(N-M+1):
        for c in range(N-M+1):
            power = 0
            for y in range(r, r+M):
                for x in range(c, c+M):
                    power += b_map[y][x]
            powers.append(power)
            ys.append(r)
            xs.append(c)

    print('#{} {} {} {}'.format(tc+1,ys[powers.index(max(powers))], xs[powers.index(max(powers))], max(powers)))
