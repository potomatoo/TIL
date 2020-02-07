import sys
sys.stdin = open('input_종이자르기.txt','r')

w, h = map(int,input().split())
n = int(input())
garo = []
sero = []

for i in range(n):
    where, idx = map(int,input().split())
    if where == 0:
        if len(garo) == 0:
            garo.append(idx)
        for j in range(len(garo)):
            if garo[j] > idx:
                garo.append(idx)
                garo[j] = garo[j] + 1
    else:
        if len(sero) == 0:
            sero.append(idx)
        for j in range(len(sero)):
            if sero[j] > idx:
                sero.append(idx)
                sero[j] = sero[j] + 1

c_map = [[0 for _ in range(w + len(sero))] for _ in range(h + len(garo))]

for i in garo:
    for y in range(len(c_map)):
        for x in range(len(c_map[y])):
            c_map[i][x] = 1

for i in sero:
    for y in range(len(c_map)):
        for x in range(len(c_map[y])):
            c_map[y][i] = 1
x_ls = []
y_ls = []
cnt = 0

for y in range(len(c_map)):
    cnt = 0
    for x in range(len(c_map[y])):
        if c_map[y][x] == 1:
            x_ls.append(cnt)
            cnt = 0
        else:
            cnt += 1
    x_ls.append(cnt)

for x in range(len(c_map[0])):
    cnt = 0
    for y in range(len(c_map)):
        if c_map[y][x] == 1:
            y_ls.append(cnt)
            cnt = 0
        else:
            cnt += 1
    y_ls.append(cnt)

print(max(x_ls)*max(y_ls))
