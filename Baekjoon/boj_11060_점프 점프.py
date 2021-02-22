N = int(input())
board = list(map(int, input().split()))
visit = [0] * N
for i in range(len(board)):
    for j in range(1, board[i]+1):
        if i+j == N:
            break
        visit[i+j] += 1

print(visit)