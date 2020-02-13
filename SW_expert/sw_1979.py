import sys
sys.stdin = open('./input/input_1979.txt','r')

TC = int(input())
for tc in range(TC):
    N, K = map(int,input().split())
    w_map = []
    k_cnt = 0
    for n in range(N):
        line = list(map(int,input().split()))
        w_map.append(line)
    for y in range(len(w_map)):
        garo = 0
        for x in range(len(w_map[y])):
            if w_map[y][x] == 0:
                if garo == K:
                    k_cnt += 1
                garo = 0
            if w_map[y][x] == 1:
                garo += 1
        if garo == K:
            k_cnt += 1

    for x in range(len(w_map[0])):
        sero = 0
        for y in range(len(w_map)):
            if w_map[y][x] == 0:
                if sero == K:
                    k_cnt += 1
                sero = 0
            if w_map[y][x] == 1:
                sero += 1
        if sero == K:
            k_cnt += 1

    print('#{} {}'.format(tc+1, k_cnt))
