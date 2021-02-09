dy = [1, 0, -1]
dx = [0, 1, -1]

def solution(n):
    answer = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    number = 2
    y, x = 0, 0
    board[y][x] = 1

    while True:
        check = number
        for i in range(3):
            y += dy[i]
            x += dx[i]
            while 0 <= y < n and 0 <= x < n and not board[y][x]:
                board[y][x] = number
                number += 1
                y += dy[i]
                x += dx[i]
            y -= dy[i]
            x -= dx[i]
        if n == 3:
            break
        if check == number:
            break

    for y in range(n):
        for x in range(n):
            if not board[y][x]:
                continue
            answer.append(board[y][x])
    return answer

print(solution(3))