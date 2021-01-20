def put_shape(shape, y, x):
    global answer
    for i in range(len(dy[shape])):
        flag = True
        mid_answer = 0

        for idx in range(len(dy[shape][i])):
            ty = y + dy[shape][i][idx]
            tx = x + dx[shape][i][idx]
            if ty < 0 or tx < 0 or ty > N-1 or tx > M-1:
                flag = False
                break
            mid_answer += board[ty][tx]

        if flag:
            answer = max(mid_answer, answer)

dy = [[(0, 0, 0, 0), (0, 1, 2, 3)],
      [(0, 0, 1, 1)],
      [(0, 1, 2, 2), (0, 0, 0, -1), (0, 0, 1, 2), (1, 0, 0, 0), (0, 0, -1, -2), (0, 0, 0, 1), (0, 0, 1, 2), (0, 1, 1, 1)],
      [(0, 1, 1, 2), (0, 0, -1, -1), (0, -1, -1, -2), (0, 0, 1, 1)],
      [(0, 0, 0, 1), (0, 1, 1, 2), (0, 0, -1, 0), (0, 0, -1, 1)]]

dx = [[(0, 1, 2, 3), (0, 0, 0, 0)],
      [(0, 1, 0, 1)],
      [(0, 0, 0, 1), (0, 1, 2, 2), (0, 1, 1, 1), (0, 0, 1, 2), (0, 1, 1, 1), (0, 1, 2, 2), (0, 1, 0, 0), (0, 0, 1, 2)],
      [(0, 0, 1, 1), (0, 1, 1, 2), (0, 0, 1, 1), (0, 1, 1, 2)],
      [(0, 1, 2, 1), (0, 0, 1, 0), (0, 1, 1, 2), (0, 1, 1, 1)]]


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
answer = 0
for k in range(5):
    for y in range(N):
        for x in range(M):
            put_shape(k, y, x)
print(answer)