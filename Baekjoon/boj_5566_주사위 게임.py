N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(int(input()))

dies = []
for _ in range(M):
    dies.append(int(input()))

check = 1
for i in range(len(dies)):
    check += dies[i]
    if check >= N:
        print(i+1)
        break
    check += board[check-1]
    if check >= N:
        print(i+1)
        break


