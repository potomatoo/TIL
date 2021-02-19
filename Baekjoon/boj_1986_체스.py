def checkQueen(y, x):
    for i in range(8):
        ty = Qdy[i] + y
        tx = Qdx[i] + x
        while 0 <= ty < N and 0 <= tx < M:
            if board[ty][tx] != 0:
                break
            byQueen.append((ty, tx))
            ty += Qdy[i]
            tx += Qdx[i]

def checkKnight(y, x):
    for i in range(8):
        ty = Kdy[i] + y
        tx = Kdx[i] + x
        if ty < 0 or ty > N-1 or tx < 0 or tx > M-1:
            continue
        byKnight.append((ty, tx))

Qdy = [0, 0, -1, 1, -1, 1, -1, 1]
Qdx = [-1, 1, 0, 0, -1, 1, 1, -1]

Kdy = [-2, -1, 1, 2, 2, 1, -1, -2]
Kdx = [1, 2, 2, 1, -1, -2, -2, -1]
N, M = map(int, input().split())
board = [[0 for _ in range(M)] for _ in range(N)]
Queen = list(map(int, input().split()))
Knight = list(map(int, input().split()))
Pawn = list(map(int, input().split()))

for i in range(1, len(Queen), 2):
    board[Queen[i]-1][Queen[i+1]-1] = 1

for i in range(1, len(Knight), 2):
    board[Knight[i]-1][Knight[i+1]-1] = 2

for i in range(1, len(Pawn), 2):
    board[Pawn[i]-1][Pawn[i+1]-1] = 3

byQueen = []
byKnight = []
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            checkQueen(y, x)
        elif board[y][x] == 2:
            checkKnight(y, x)

for y, x in byQueen:
    board[y][x] = 1
for y, x in byKnight:
    board[y][x] = 2

answer = 0
for z in range(N):
    answer += board[z].count(0)
print(answer)