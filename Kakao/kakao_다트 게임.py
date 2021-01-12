def solution(dartResult):
    board = [0, 0, 0]
    visit = [0, 0, 0]
    idx = 0
    for i in range(len(dartResult)):
        if dartResult[i].isnumeric():
            if dartResult[i+1] == '0':
                board[idx] = 10
                visit[idx] = 1
                continue
            if not visit[idx]:
                board[idx] = int(dartResult[i])
                visit[idx] = 1
            idx += 1
        elif dartResult[i] == 'D':
            board[idx-1] **= 2
        elif dartResult[i] == 'T':
            board[idx-1] **= 3
        elif dartResult[i] == '#':
            board[idx-1] *= -1
        elif dartResult[i] == '*':
            if idx == 0:
                board[idx-1] *= 2
            else:
                board[idx-1] *= 2
                board[idx-2] *= 2

    return sum(board)

print(solution('10D10S#10S'))