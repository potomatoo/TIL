import sys
sys.stdin = open('./input/input_omok.txt','r')

o_map = []
for _ in range(19):
    line = list(map(int,input().split()))
    o_map.append(line)

dx = [1, 0, 1, 1]
dy = [0, 1, -1, 1]
result = 0
flag = True
for y in range(len(o_map)):
    for x in range(len(o_map[y])):
        if o_map[y][x] == 0:
            continue
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or ty > 18 or tx < 0 or tx > 18:
                continue
            if o_map[ty][tx] != o_map[y][x]:
                continue
            cnt = 0
            while True:
                if o_map[ty][tx] != o_map[y][x]:
                    break
                else:
                    ty = ty + dy[i]
                    tx = tx + dx[i]
                    cnt += 1
                    if ty < 0 or ty > 18 or tx < 0 or tx > 18:
                        break


            if cnt == 4:
                ty = y - dy[i]
                tx = x - dx[i]
                if ty < 0 or tx < 0:
                    print(o_map[y][x])
                    print(y + 1, x + 1)
                    flag = False
                    result += 1
                    break

                elif o_map[ty][tx] != o_map[y][x]:
                    print(o_map[y][x])
                    print(y+1, x+1)
                    flag = False
                    result += 1
                    break

    if flag == False:
        break
if result == 0:
    print(0)

