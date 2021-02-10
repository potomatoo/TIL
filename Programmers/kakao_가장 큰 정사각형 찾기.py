def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    for y in range(1, N):
        for x in range(1, M):
            if board[y][x] >= 1:
                now = min(board[y][x-1], board[y-1][x], board[y-1][x-1]) + 1
                board[y][x] = now

    for z in range(N):
        answer = max(max(board[z]), answer)

    return answer ** 2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))