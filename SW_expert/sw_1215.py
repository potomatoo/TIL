import sys
sys.stdin = open('./input/input_1215.txt','r')

def get_reverse(a):
    reverse_ = ''
    for i in range(len(a)-1,-1,-1):
        reverse_ += a[i]
    if reverse_ == a:
        return True
    else:
        return False

for tc in range(10):
    n = int(input())
    p_map = []
    for _ in range(8):
        p_map.append(input())

    cnt = 0
    garo = []
    for y in range(len(p_map)):
        for x in range(len(p_map)-(n-1)):
            garo.append(p_map[y][x:x+n])

    for y in range(len(garo)):
        if get_reverse(garo[y]):
            cnt += 1

    p_map2 = []
    for x in range(8):
        line = ''
        for y in range(8):
            line += p_map[y][x]
        p_map2.append(line)
    sero = []
    for y in range(len(p_map2)):
        for x in range(len(p_map2)-(n-1)):
            sero.append(p_map2[y][x:x+n])

    for y in range(len(sero)):
        if get_reverse(sero[y]):
            cnt += 1

    print('#{} {}'.format(tc+1, cnt))
