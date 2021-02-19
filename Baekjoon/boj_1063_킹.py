move_dic = {
    'R': 0,
    'L': 1,
    'B': 2,
    'T': 3,
    'RT': 4,
    'LT': 5,
    'RB': 6,
    'LB': 7
}

col_dic = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

rcol_dic = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H'
}

dy = [0, 0, 1, -1, -1, -1, 1, 1]
dx = [1, -1, 0, 0, 1, -1, 1, -1]

king, dol, N = input().split()

board = [[0 for _ in range(8)] for _ in range(8)]
ky, kx = 8-int(king[1]), col_dic[king[0]]
board[ky][kx] = 1
oy, ox = 8-int(dol[1]), col_dic[dol[0]]
board[oy][ox] = 2
for _ in range(int(N)):
    move = input()
    kty = dy[move_dic[move]] + ky
    ktx = dx[move_dic[move]] + kx
    if kty < 0 or ktx < 0 or kty > 7 or ktx > 7:
        continue
    if board[kty][ktx] == 2:
        oty = dy[move_dic[move]] + oy
        otx = dx[move_dic[move]] + ox
        if oty < 0 or otx < 0 or oty > 7 or otx > 7:
            continue
        board[kty][ktx] = 1
        board[oty][otx] = 2
        board[ky][kx] = 0
        ky, kx, oy, ox = kty, ktx, oty, otx
    else:
        board[kty][ktx] = 1
        board[ky][kx] = 0
        ky, kx = kty, ktx

print('{}{}'.format(rcol_dic[kx], 8-ky))
print('{}{}'.format(rcol_dic[ox], 8-oy))