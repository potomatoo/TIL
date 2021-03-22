def split_ground(i, j, n):
    global answer
    if n == 0:
        return
    left = right = down = up = 0
    for y in range(N):
        for x in range(j, j+(n//2)):
            left = max(left, board[y][x])

    for y in range(N):
        for x in range(j+(n//2), N):
            right = max(right, board[y][x])

    for y in range(i+n//2, N):
        for x in range(N):
            down = max(down, board[y][x])

    for y in range(i+n//2):
        for x in range(N):
            up = max(up, board[y][x])
    answer += max(left, right, down, up)

    split_ground(i, j, n//2)


N = int(input())
answer = 0
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
split_ground(0, 0, N)
print(answer)