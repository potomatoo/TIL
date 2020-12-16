import sys
sys.stdin = open('./input/input_1974.txt','r')

def get_turn(n_map):
    new_map = []
    for x in range(len(n_map[0])):
        other_map = []
        for y in range(len(n_map)-1,-1,-1):
            other_map.append(n_map[y][x])
        new_map.append(other_map)
    return new_map

TC = int(input())
for tc in range(TC):
    s_map = []
    for _ in range(9):
        s_map.append(list(map(int,input().split())))

    result = 1
    for y in range(len(s_map)):
        check = set()
        for x in range(len(s_map[y])):
            check.add(s_map[y][x])

        if len(check) != 9:
            result -= 1
            break

    garo = get_turn(s_map)
    for y in range(len(garo)):
        check = set()
        for x in range(len(garo[y])):
            check.add(garo[y][x])

        if len(check) != 9:
            result -= 1
            break

    for r in range(0,7,3):
        for c in range(0,7,3):
            check = set()
            for y in range(r,r+3):
                for x in range(c,c+3):
                    check.add(s_map[y][x])


            if len(check) != 9:
                result -= 1
                break

    if result == 1:
        print('#{} {}'.format(tc+1,1))
    else:
        print('#{} {}'.format(tc+1,0))