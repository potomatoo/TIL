import sys
sys.stdin = open('./input/input_11315.txt', 'r')

def find_omok(y, x):
    for i in range(8):
        check = 0
        yy, xx = y, x
        while True:
            ty = yy + dy[i]
            tx = xx + dx[i]
            if ty < 0 or tx < 0 or ty > N-1 or tx > N-1:
                break
            if board[ty][tx] == '.':
                break
            if board[ty][tx] == 'o':
                check += 1
            yy, xx = ty, tx
        if check >= 4:
            return True
    return False

dy = [-1, 1, 0, 0, -1, 1, -1, 1]
dx = [0, 0, -1, 1, -1, 1, 1, -1]

TC = int(input())
for tc in range(TC):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(input())

    flag = False
    for y in range(N):
        for x in range(N):
            if board[y][x] == 'o':
                if find_omok(y, x):
                    flag = True
                    break
        if flag:
            break

    if flag:
        print('#{} {}'.format(tc+1, 'YES'))
    else:
        print('#{} {}'.format(tc + 1, 'NO'))