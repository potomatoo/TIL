def build(board):
    visit = [0] * N
    for i in range(len(board)-1):
        if board[i] == board[i+1]:
            continue
        if abs(board[i] - board[i+1]) >= 2:
            return False
        if board[i] > board[i+1]:
            cnt = 0
            for d in range(i+1, i+1+L):
                if d > N-1:
                    break
                if board[d] != board[i+1]:
                    break
                if visit[d]:
                    return False
                cnt += 1
                visit[d] = 1
            if cnt < L:
                return False

        if board[i] < board[i+1]:
            cnt = 0
            for d in range(i, i-L, -1):
                if d < 0:
                    break
                if board[d] != board[i]:
                    break
                if visit[d]:
                    return False
                visit[d] = 1
                cnt += 1
            if cnt < L:
                return False
    return True

N, L = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

board2 = []
for x in range(N):
    one = []
    for y in range(N):
        one.append(board[y][x])
    board2.append(one)

answer = 0
for i in range(len(board)):
    if build(board[i]):
        answer += 1

for i in range(len(board2)):
    if build(board2[i]):
        answer += 1

print(answer)