dy = [1, 0, -1]
dx = [0, 1, -1]

def solution(n):
    answer = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    y, x, num = 0, 0, 1
    while True:
        flag = False
        for i in range(3):
            while 0 <= y < n and 0 <= x < n and not visit[y][x]:
                flag = True
                board[y][x] = num
                visit[y][x] = 1
                y += dy[i]
                x += dx[i]
                num += 1
            if i == 0:
                y -= 1
                x += 1
            elif i == 1:
                y -= 1
                x -= 2
            elif i == 2:
                y += 2
                x += 1
        if not flag:
            break

    for y in range(n):
        for x in range(y+1):
            if board[y][x]:
                answer.append(board[y][x])

    return answer

print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))