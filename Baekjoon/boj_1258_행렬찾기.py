import sys
sys.stdin = open('./input/input_1258.txt','r')

TC = int(input())
for tc in range(TC):
    N = int(input())
    o_map = []
    result = []
    for _ in range(N):
        o_map.append(list(map(int,input().split())))
    visit = [[0 for _ in range(N)]for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if o_map[y][x] == 0 or visit[y][x] == 1:
                continue
            visit[y][x] = 1
            ty = y + 1
            tx = x + 1
            while o_map[ty][x] != 0 and visit[ty][x] == 0:
                visit[ty][x] = 1
                ty = ty + 1
            while o_map[y][tx] != 0 and visit[y][tx] == 0:
                visit[y][tx] = 1
                tx = tx + 1
            for i in range(y,ty+1):
                for j in range(x,tx+1):
                    visit[i][j] = 1
            result.append((ty-y,tx-x))
    for i in range(len(result)-1):
        for j in range(i+1,len(result)):
            if result[i][0] * result[i][1] == result[j][0] * result[j][1]:
                if result[i][0] > result[j][0]:
                    result[i],result[j] = result[j], result[i]
            if result[i][0] * result[i][1] > result[j][0] * result[j][1]:
                result[i], result[j] = result[j], result[i]
    print('#%d'%(tc+1),end=' ')
    print(len(result),end=' ')
    for i in range(len(result)):
        if i == len(result)-1:
            print(result[i][0], end= ' ')
            print(result[i][1])
        else:
            print(result[i][0],end=' ')
            print(result[i][1],end=' ')






