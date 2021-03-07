def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    board = [0] * (n+1)
    board[1] = 1
    board[2] = 2
    for i in range(3, n+1):
        board[i] = board[i-1] + board[i-2]

    return board[n] % 1234567

print(solution(4))
print(solution(3))