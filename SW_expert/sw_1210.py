import sys
sys.stdin = open('./input/input_1210.txt','r')

for tc in range(10):
    n = int(input())
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int,input().split())))
    visit = [[0 for _ in range(100)] for _ in range(100)]
    dy = [0, 0, -1]
    dx = [-1, 1, 0]

    x = 0
    y = 99
    for i in range(len(ladder[-1])):
        if ladder[-1][i] == 2:
            x = i

    while True:
        if y == 0:
            break
        for i in range(3):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or tx < 0 or ty > 99 or tx > 99:
                continue
            if visit[ty][tx] == 0 and ladder[ty][tx] == 1:
                visit[y][x] = 1
                y, x = ty, tx
                break
    print('#{} {}'.format(tc+1,x))
