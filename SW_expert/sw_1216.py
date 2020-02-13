import sys
sys.stdin = open('./input/input_1216.txt','r')

def get_reverse(a):
    reverse_ = ''
    for i in range(len(a)-1,-1,-1):
        reverse_ += a[i]
    if reverse_ == a:
        return True
    else:
        return False

def get_long(words):
    long = 0
    flag = True
    for k in range(len(words),-1,-1):
        for i in range(len(words)-(k-1)):
            if get_reverse(words[i:i+k]) == True:
                long += len(words[i:i+k])
                flag = False
                break
        if flag == False:
            break
    return long

for _ in range(10):
    tc = int(input())
    p_map = []
    for _ in range(100):
        line = input()
        p_map.append(line)

    p_map2 = []
    for x in range(100):
        line = ''
        for y in range(100):
            line += p_map[y][x]
        p_map2.append(line)

    garo_max = get_long(p_map[0])
    for y in range(1,100):
        if garo_max < get_long(p_map[y]):
            garo_max = get_long(p_map[y])

    sero_max = get_long(p_map2[0])
    for y in range(1,100):
        if sero_max < get_long(p_map2[y]):
            sero_max = get_long(p_map2[y])

    if garo_max > sero_max:
        print('#{} {}'.format(tc,garo_max))
    else:
        print('#{} {}'.format(tc, sero_max))
