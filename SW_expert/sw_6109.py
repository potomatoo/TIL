import sys
sys.stdin = open('./input/input_6109.txt','r')

def go_right(t_map):
    for y in range(len(t_map)):
        for i in range(t_map[y].count(0)):
            t_map[y].remove(0)
        for i in range(N - len(t_map[y])):
            t_map[y].insert(0,0)
    for y in range(len(t_map)):
        for x in range(len(t_map[y])-1,0,-1):
            if t_map[y][x] == t_map[y][x-1]:
                t_map[y][x] = t_map[y][x] + t_map[y][x-1]
                t_map[y][x-1] = 0
    for y in range(len(t_map)):
        for i in range(t_map[y].count(0)):
            t_map[y].remove(0)
        for i in range(N - len(t_map[y])):
            t_map[y].insert(0,0)
    return t_map

def go_left(t_map):
    for y in range(len(t_map)):
        for i in range(t_map[y].count(0)):
            t_map[y].remove(0)
        for i in range(N - len(t_map[y])):
            t_map[y].insert(N-1,0)
    for y in range(len(t_map)):
        for x in range(len(t_map[y])-1):
            if t_map[y][x] == t_map[y][x+1]:
                t_map[y][x] = t_map[y][x] + t_map[y][x+1]
                t_map[y][x+1] = 0
    for y in range(len(t_map)):
        for i in range(t_map[y].count(0)):
            t_map[y].remove(0)
        for i in range(N - len(t_map[y])):
            t_map[y].insert(N-1,0)
    return t_map

def go_up(t_map, N):
    nt_map = []
    for x in range(N):
        line = []
        for y in range(len(t_map)):
            line.append(t_map[y][x])
        nt_map.append(line)
    nt_map = go_left(nt_map)
    t_map = []
    for x in range(N):
        line = []
        for y in range(len(nt_map)):
            line.append(nt_map[y][x])
        t_map.append(line)
    return t_map

def go_down(t_map, N):
    nt_map = []
    for x in range(N):
        line = []
        for y in range(len(t_map)):
            line.append(t_map[y][x])
        nt_map.append(line)
    nt_map = go_right(nt_map)
    t_map = []
    for x in range(N):
        line = []
        for y in range(len(nt_map)):
            line.append(nt_map[y][x])
        t_map.append(line)
    return t_map


TC = int(input())
for tc in range(TC):
    N, S = map(str,input().split())
    N = int(N)
    t_map = []
    for n in range(N):
        line = list(map(int,input().split()))
        t_map.append(line)
    if S == 'right':
        t_map = go_right(t_map)
    if S == 'left':
        t_map = go_left(t_map)
    if S == 'up':
        t_map = go_up(t_map,N)
    if S == 'down':
        t_map = go_down(t_map,N)
    print('#%d'%(tc+1))
    for y in range(len(t_map)):
        for x in range(len(t_map[y])):
            print(t_map[y][x], end=' ')
        print()





