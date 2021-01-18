def work():
    global cnt
    while True:
        board.rotate(1)
        robot.rotate(1)
        robot[N-1] = 0
        for i in range(N-2, -1, -1):
            if robot[i] and not robot[i+1] and board[i+1] > 0:
                board[i+1] -= 1
                robot[i+1] = 1
                robot[i] = 0
        robot[N-1] = 0

        if not robot[0] and board[0] > 0:
            board[0] -= 1
            robot[0] = 1
        flag = 0
        for i in range(len(board)):
            if board[i] == 0:
                flag += 1
        if flag >= K:
            break
        cnt += 1

from collections import deque
N, K = map(int, input().split())
board = deque(map(int, input().split()))
cnt = 1
robot = deque([0] * len(board))
work()
print(cnt)