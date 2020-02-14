import sys
sys.stdin = open('./input/input_1961.txt','r')

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
    N = int(input())
    n_map = []
    for _ in range(N):
        n_map.append(list(map(int,input().split())))
    result = []
    for _ in range(3):
        n_map = get_turn(n_map)
        result.append(n_map)
    print('#%d'%(tc+1))

    for x in range(len(result[0][0])):
        for y in range(len(result)):
            if y != 0:
                print(end=' ')
            for k in range(N):
                print(result[y][x][k], end='')
        print()