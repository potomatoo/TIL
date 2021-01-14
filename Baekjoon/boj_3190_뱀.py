N = int(input())
apple = []
k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    apple.append((y-1, x-1))
L = int(input())
move = []
for _ in range(L):
    move.append(input().split())

y, x = 0, 0
snake = [(0, 0)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
idx = 0
cnt = 0
while True:
    cnt += 1
    ty = dy[idx] + y
    tx = dx[idx] + x
    if ty < 0 or ty > N-1 or tx < 0 or tx > N-1 or (ty, tx) in snake:
        break
    if (ty, tx) in apple:
        apple.remove((ty, tx))
        snake.append((ty, tx))
    else:
        snake.append((ty, tx))
        snake.pop(0)

    for time, d in move:
        if int(time) == cnt:
            if d == 'D':
                if idx == 3:
                    idx = 0
                else:
                    idx += 1
            else:
                if idx == 0:
                    idx = 3
                else:
                    idx -= 1
    y, x = ty, tx

print(cnt)

