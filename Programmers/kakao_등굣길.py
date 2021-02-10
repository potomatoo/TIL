def solution(m, n, puddles):
    board = [[1] * m for _i in range(n)]

    for x, y in puddles:
        board[y - 1][x - 1] = 0
        if x - 1 == 0:
            for k in range(y - 1, n):
                board[k][0] = 0
        if y - 1 == 0:
            for k in range(x - 1, m):
                board[0][k] = 0

    for i in range(1, n):
        for j in range(1, m):
            if i * j != 0:
                if board[i][j] != 0:
                    board[i][j] = board[i - 1][j] + board[i][j - 1]
    answer = board[n - 1][m - 1]
    return answer % 1000000007

print(solution(4, 3, [[1,2]]))