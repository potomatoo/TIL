N, M = map(int, input().split())
board1 = []
board2 = []
for i in range(1, N+1):
    mid_board1 = ''
    mid_board2 = ''
    if M % 2:
        if i % 2:
            mid_board1 += ('WB' * (M // 2) + 'W')
            mid_board2 += ('BW' * (M // 2) + 'B')
        else:
            mid_board1 += ('BW' * (M // 2) + 'B')
            mid_board2 += ('WB' * (M // 2) + 'W')
    else:
        if i % 2:
            mid_board1 += 'WB' * (M//2)
            mid_board2 += 'BW' * (M//2)
        else:
            mid_board1 += 'BW' * (M // 2)
            mid_board2 += 'WB' * (M // 2)
    one1 = ','.join(mid_board1)
    board1.append(one1.split(','))
    one2 = ','.join(mid_board2)
    board2.append(one2.split(','))


board = []
for _ in range(N):
    step1 = ','.join(input())
    step2 = step1.split(',')
    board.append(step2)

dif1 = 1e9
dif2 = 1e9
for y in range(N):
    for x in range(M):
        check_board = ''
        check_board1 = ''
        check_board2 = ''
        mid_dif1 = 0
        mid_dif2 = 0
        if y+8 > N or x+8 > M:
            continue
        for yy in range(y, y+8):
            for xx in range(x, x+8):
                check_board += board[yy][xx]
                check_board1 += board1[yy][xx]
                check_board2 += board2[yy][xx]
        if check_board != check_board1:
            for i in range(len(check_board)):
                if check_board[i] != check_board1[i]:
                    mid_dif1 += 1
        if check_board != check_board2:
            for i in range(len(check_board)):
                if check_board[i] != check_board2[i]:
                    mid_dif2 += 1
        dif1 = min(dif1, mid_dif1)
        dif2 = min(dif2, mid_dif2)

print(min(dif1, dif2))
