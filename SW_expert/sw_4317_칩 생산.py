import sys
sys.stdin = open('./input/input_4317.txt','r')

def get_square(y, x):
    area = 0
    visit = [(y, x)]
    for i in range(3):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
            return False
        if board[ty][tx] == 1:
            return False
        visit.append((ty, tx))
        area += 1

    if area == 3:
        square.append(visit)

def find_max(k):
    global answer
    if k == len(square):
        answer = max(answer, len(check))
        print(check)
        return
    else:
        for i in range(len(square)):
            if visit[i]:
                continue
            visit[i] = 1
            check.append(square[i])
            find_max(k+1)
            visit[i] = 0
            check.pop()

dy = [1, 1, 0]
dx = [0, 1, 1]

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    answer = 0
    square = []
    for y in range(N):
        for x in range(M):
            if not board[y][x]:
                get_square(y, x)

    square = [0, 1, 2, 3, 4]
    visit = [0] * len(square)
    check = []

    find_max(0)

    print('#{} {}'.format(tc+1, answer))

