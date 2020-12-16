def go_right(y, x, t):
    if blue[y][x] == 3 or x == 9:
        if t == 1:
            board[y][x] = 3
            blue[y][x-4] = 1
        elif t == 2:
            board[y][x] = 3
            board[y][x-1] = 3
            blue[y][x - 4] = 1
            blue[y][x - 5] = 1
        elif t == 3:
            board[y][x] = 3
            board[y-1][x] = 3
            blue[y][x - 4] = 1
            blue[y-1][x - 4] = 1
        return
    go_right(y, x+1, t)

def go_down(y, x, t):
    if board[y][x] == 3 or y == 9:
        if t == 1:
            board[y][x] = 3
            green[y-4][x] = 1
        elif t == 2:
            board[y][x] = 3
            board[y][x-1] = 3
            green[y-4][x] = 1
            green[y-4][x-1] = 1
        elif t == 3:
            board[y][x] = 3
            board[y-1][x] = 3
            green[y-4][x] = 1
            green[y-5][x] = 1
        return
    go_down(y+1, x, t)


board = [[0 for _ in range(10)] for _ in range(10)]
for y in range(10):
    for x in range(10):
        if y > 3 and x < 4:
            board[y][x] = 1
        elif y < 4 and x > 3:
            board[y][x] = 2
        elif y > 3 and x > 3:
            board[y][x] = 3

for z in range(10):
    print(board[z])

N = int(input())
blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]
score = 0



