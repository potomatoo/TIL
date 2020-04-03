import sys
sys.stdin = open('./input/input_5427.txt', 'r')

from _collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
TC = int(input())
for _ in range(TC):
    M, N = map(int,input().split())
    building = [list(map(str, [*input()])) for _ in range(N)]
    fire = deque()
    start = deque()
    visit_f = [[0 for _ in range(M)] for _ in range(N)]
    visit_s = [[0 for _ in range(M)] for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if building[y][x] == '*':
                fire.append((y, x))
                visit_f[y][x] = 1
            if building[y][x] == '@':
                start.append((y, x, 1))
                visit_s[y][x] = 1

    flag = True

    while start:
        for z in range(N):
            print(building[z])
        print()
        if len(fire) > 0:
            fy, fx = fire.popleft()
            for i in range(4):
                tfy = fy + dy[i]
                tfx = fx + dx[i]
                if tfy < 0 or tfx < 0 or tfy > N - 1 or tfx > M - 1:
                    continue
                if building[tfy][tfx] != '#' and visit_f[tfy][tfx] == 0:
                    visit_f[tfy][tfx] = 1
                    building[tfy][tfx] = '*'
                    fire.append((tfy, tfx))

        sy, sx, sd = start.popleft()
        if sy == 0 or sx == 0 or sy == N-1 or sx == M-1:
            print(sd)
            flag = False
            break
        for i in range(4):
            tsy = sy + dy[i]
            tsx = sx + dx[i]
            if tsy < 0 or tsx < 0 or tsy > N-1 or tsx > M-1:
                continue
            if building[tsy][tsx] == '.' and visit_s[tsy][tsx] == 0:
                visit_s[tsy][tsx] = 1
                building[tsy][tsx] = '@'
                start.append((tsy, tsx, sd+1))

    if flag:
        print('IMPOSSIBLE')





