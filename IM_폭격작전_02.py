import sys
sys.stdin = open('./input/input_폭격작전_02.txt','r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))
    bomb = [[0 for _ in range(N)] for _ in range(N)]
    sum_ = 0
    for m in range(M):
        bomb_r, bomb_c, bomb_s = map(int, input().split())
        r_end = bomb_r + bomb_s
        c_end = bomb_c + bomb_s
        if r_end > N:
            r_end = N
        if c_end > N:
            c_end = N
        for i in range(bomb_r, r_end):
            for j in range(bomb_c, c_end):
                if not bomb[i][j]:
                    sum_ += board[i][j]
                    bomb[i][j] = 1
    print('#{0} {1}'.format(t, sum_))