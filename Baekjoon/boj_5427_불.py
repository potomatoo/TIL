import sys
sys.stdin = open('./input/input_5427(2).txt', 'r')

from _collections import deque

TC = int(input())
for tc in range(TC):
    M, N = map(int, input().split())
    building = [list(map(str, [*input()])) for _ in range(N)]
    fire = []
    person = deque()
    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit_f = [[0 for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if building[y][x] == '*':
                fire.append((y, x))
                visit_f[y][x] = 1
            if building[y][x] == '@':
                person.append((y, x, 0))
                visit[y][x] = 1

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    check_fire = [0] * (1001 * 1001)
    flag = True

    while person:

        y, x, k = person.popleft()

        if check_fire[k] == 0:
            check_fire[k] = 1
            new_fire = []
            for fy, fx in fire:
                for i in range(4):
                    fty = fy + dy[i]
                    ftx = fx + dx[i]
                    if fty < 0 or ftx < 0 or fty > N-1 or ftx > M-1:
                        continue
                    if building[fty][ftx] == '.' and visit_f[fty][ftx] == 0:
                        visit_f[fty][ftx] = 1
                        new_fire.append((fty, ftx))
                        building[fty][ftx] = '*'
            fire = new_fire

        if y == 0 or y == N-1 or x == 0 or x == M-1:
            print(k+1)
            flag = False
            break

        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
                continue
            if building[ty][tx] == '.' and visit[ty][tx] == 0:
                visit[ty][tx] = 1
                person.append((ty, tx, k+1))

    if flag:
        print('IMPOSSIBLE')




