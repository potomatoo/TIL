from copy import deepcopy

def go_right(c_map):
    for y in range(len(c_map)):
        for i in range(c_map[y].count(0)):
            c_map[y].remove(0)
        for i in range(N - len(c_map[y])):
            c_map[y].insert(0,0)
    for y in range(len(c_map)):
        for x in range(len(c_map[y])-1,0,-1):
            if c_map[y][x] == c_map[y][x-1]:
                c_map[y][x] = c_map[y][x] + c_map[y][x-1]
                c_map[y][x-1] = 0
    for y in range(len(c_map)):
        for i in range(c_map[y].count(0)):
            c_map[y].remove(0)
        for i in range(N - len(c_map[y])):
            c_map[y].insert(0,0)
    return c_map

def go_left(c_map):
    for y in range(len(c_map)):
        for i in range(c_map[y].count(0)):
            c_map[y].remove(0)
        for i in range(N - len(c_map[y])):
            c_map[y].insert(N-1,0)
    for y in range(len(c_map)):
        for x in range(len(c_map[y])-1):
            if c_map[y][x] == c_map[y][x+1]:
                c_map[y][x] = c_map[y][x] + c_map[y][x+1]
                c_map[y][x+1] = 0
    for y in range(len(c_map)):
        for i in range(c_map[y].count(0)):
            c_map[y].remove(0)
        for i in range(N - len(c_map[y])):
            c_map[y].insert(N-1,0)
    return c_map

def go_up(c_map):
    nt_map = []
    for x in range(N):
        line = []
        for y in range(len(c_map)):
            line.append(c_map[y][x])
        nt_map.append(line)
    nt_map = go_left(nt_map)
    c_map = []
    for x in range(N):
        line = []
        for y in range(len(nt_map)):
            line.append(nt_map[y][x])
        c_map.append(line)

    return c_map

def go_down(c_map):
    nt_map = []
    for x in range(N):
        line = []
        for y in range(len(c_map)):
            line.append(c_map[y][x])
        nt_map.append(line)
    nt_map = go_right(nt_map)
    c_map = []
    for x in range(N):
        line = []
        for y in range(len(nt_map)):
            line.append(nt_map[y][x])
        c_map.append(line)

    return c_map

def Permutation(k):
    global ans
    global middle_check
    if k == 4:
        for t in range(4):
            order.append(arr[t])
            c_map = deepcopy(t_map)
            for j in range(5):
                if order[j] == 'up':
                    c_map = go_up(c_map)
                    a = 1
                if order[j] == 'down':
                    c_map = go_down(c_map)
                    a = 1
                if order[j] == 'right':
                    c_map = go_right(c_map)
                    a = 1
                if order[j] == 'left':
                    c_map = go_left(c_map)
                    a = 1

                flag = True
                for yy in range(N):
                    for xx in range(N):
                        if c_map[yy][xx] > middle_check:
                            middle_check = c_map[yy][xx]
                            flag = False
                            break
                    if not flag:
                        break

                if middle_check > ans:
                    ans = middle_check
                    break
            order.pop()

    else:
        for i in range(4):
            order.append(arr[i])
            Permutation(k+1)
            order.pop()

N = int(input())
t_map = []

for _ in range(N):
    t_map.append(list(map(int, input().split())))

arr = ['up', 'down', 'right', 'left']
order = []
middle_check = 0
ans = 0
Permutation(0)
print(ans)