from _collections import deque
N, M, T = map(int,input().split())
Q = deque()
pan = deque()
for _ in range(N):
    pan.append(Q)
for i in range(N):
    pan[i] = deque(map(int,input().split()))

dy = [1, 0]
dx = [0, 1]

for _ in range(T):
    
    xj, d, k = map(int,input().split())
    for i in range(len(pan)):
        if (i+1) % xj == 0:
            if d == 0:
                pan[i].rotate(k)
            elif d == 1:
                pan[i].rotate(-k)
    close = 0
    change = set()
    for y in range(N):
        for x in range(M):
            if x == 0 and pan[y][x] == pan[y][M-1] and pan[y][x] != 0:
                change.add((y, x))
                change.add((y, x+(M-1)))
                close += 1
            for i in range(2):
                ty = y + dy[i]
                tx = x + dx[i]
                if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
                    continue
                if pan[y][x] == pan[ty][tx] and pan[y][x] != 0:
                    close += 1
                    change.add((y,x))
                    change.add((ty,tx))
                    while True:
                        ty = ty + dy[i]
                        tx = tx + dx[i]
                        if ty < 0 or tx < 0 or ty > N - 1 or tx > M - 1:
                            break
                        if pan[y][x] != pan[ty][tx]:
                            break
                        change.add((ty, tx))

    for y, x in change:
        pan[y][x] = 0

    if close == 0:
        summ = 0
        num = 0
        for y in range(N):
            for x in range(M):
                if pan[y][x] != 0:
                    num += 1
                    summ += pan[y][x]
        if summ == 0 or num == 0:
            break
        avg = summ / num
        for y in range(N):
            for x in range(M):
                if pan[y][x] != 0 and pan[y][x] > avg:
                    pan[y][x] -= 1
                elif pan[y][x] != 0 and pan[y][x] < avg:
                    pan[y][x] += 1

cnt = 0
for y in range(N):
    for x in range(M):
        cnt += pan[y][x]
print(cnt)
