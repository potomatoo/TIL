from copy import deepcopy
from _collections import deque

def combination(k):
    if k == 7:
        win = 0
        for y, x in c_order:
            if school[y][x] == 'S':
                win += 1
            if win > 3:
                w_order = deepcopy(c_order)
                win_s.append(w_order)
                break

    else:
        for i in range(25):
            if visit1[i] == 1:
                continue
            if len(c_order) > 0:
                if c_order[-1] > classmate[i]:
                    continue
            visit1[i] = 1
            c_order.append(classmate[i])
            combination(k+1)
            visit1[i] = 0
            c_order.pop()

school = []
for _ in range(5):
    school.append(input())

classmate = []
for y in range(5):
    for x in range(5):
        classmate.append((y,x))

s_order = []
c_order = []
visit1 = [0] * 25
win_s = []

combination(0)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
for k in range(len(win_s)):
    flag = True
    Q = deque()
    visit2 = [[0 for _ in range(5)] for _ in range(5)]
    Q.append(win_s[k][0])
    visit2[win_s[k][0][0]][win_s[k][0][1]] = 1
    while Q:
        yy, xx = Q.popleft()
        for i in range(4):
            ty = yy + dy[i]
            tx = xx + dx[i]
            if ty < 0 or tx < 0 or ty > 4 or tx > 4:
                continue
            if (ty, tx) in win_s[k] and visit2[ty][tx] == 0:
                visit2[ty][tx] = 1
                Q.append((ty, tx))

    for cy, cx in win_s[k]:
        if visit2[cy][cx] != 1:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)