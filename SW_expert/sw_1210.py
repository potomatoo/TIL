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
    ty = 99
    tx = 0
    for i in range(len(ladder[-1])):
        if ladder[-1][i] == 2:
            tx = i

    while True:
        if ty == 0:
            break
        for i in range(3):
            ty = ty + dy[i]
            tx = tx + dx[i]
            if tx < 0 or tx > 99:
                continue
            if ladder[ty][tx] == 1 and visit[ty][tx] == 0:
                visit[ty][tx] = 1
                break
        print(ty,tx)

