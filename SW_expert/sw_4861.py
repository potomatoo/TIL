import sys
sys.stdin = open('./input/input_4861.txt','r')

TC = int(input())
for tc in range(TC):
    N, M = map(int,input().split())
    pallidrone = []
    for i in range(N):
        line = input()
        pallidrone.append(line)

    garo = []
    garo1 = []
    for y in range(len(pallidrone)):
        for i in range(len(pallidrone[y])-(M-1)):
            pallidrone1 = pallidrone[y][i:i+M]
            garo1.append(pallidrone1)

    for y in range(len(garo1)):
        reverse_ = ''
        for k in range(len(garo1[y])-1,-1,-1):
            reverse_ += garo1[y][k]
        if reverse_ == garo1[y]:
            garo.append(garo1[y])

    pallidrone2 = []
    sero = []
    sero1 = []
    for x in range(N):
        sero2 = ''
        for y in range(len(pallidrone)):
            sero2 += pallidrone[y][x]
        pallidrone2.append(sero2)

    for y in range(len(pallidrone2)):
        for i in range(len(pallidrone2[y])-(M-1)):
            pallidrone3 = pallidrone2[y][i:i+M]
            sero1.append(pallidrone3)

    for y in range(len(sero1)):
        reverse2_ = ''
        for k in range(len(sero1[y])-1,-1,-1):
            reverse2_ += sero1[y][k]
        if reverse2_ == sero1[y] and len(sero1[y]) == M:
            sero.append(sero1[y])
    result = garo + sero
    print('#%d'%(tc+1), end=' ')
    for i in range(len(result)):
        if i == len(result)-1:
            print(result[i])
        else:
            print(result[i],end=' ')


