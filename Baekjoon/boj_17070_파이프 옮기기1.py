import sys
from collections import deque

def is_range(y, x):
    if y < 0 or y > N-1 or x < 0 or x > N-1:
        return False
    return True

def push_pipe(d, y, x):
    if d == 1:
        if is_range(y, x+1) and not board[y][x+1]:
            Q.append((1, y, x, y, x+1))
        if is_range(y+1, x+1) and not board[y+1][x] and not board[y][x+1] and not board[y+1][x+1]:
            Q.append((3, y, x, y+1, x+1))
    elif d == 2:
        if is_range(y+1, x) and not board[y+1][x]:
            Q.append((2, y, x, y+1, x))
        if is_range(y+1, x+1) and not board[y+1][x] and not board[y][x+1] and not board[y+1][x+1]:
            Q.append((3, y, x, y+1, x+1))
    else:
        if is_range(y, x+1) and not board[y][x+1]:
            Q.append((1, y, x, y, x+1))
        if is_range(y+1, x) and not board[y+1][x]:
            Q.append((2, y, x, y+1, x))
        if is_range(y+1, x+1) and not board[y+1][x] and not board[y][x+1] and not board[y+1][x+1]:
            Q.append((3, y, x, y+1, x+1))


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

Q = deque()
Q.append((1, 0, 0, 0, 1))
answer = 0
while Q:
    d, y, x, yy, xx = Q.popleft()
    if yy == N-1 and xx == N-1:
        answer += 1
        continue
    push_pipe(d, yy, xx)

print(answer)