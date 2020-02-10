import sys
sys.stdin = open('./input/input_omok.txt','r')

board = []
result = []
for _ in range(19):
    line = list(map(int, input().split()))
    board.append(line)
for y in range(len(board)):
    for x in range(len(board[y])-4):
        summ = 0
        check = set()

        for i in range(5):
            summ += board[y][x+i]
            check.add(board[y][x+i])
        check = list(check)

        if len(check) == 1:
            if x == 0 and board[y][x+5] != check[0]:
                if summ == 5 or summ == 10:
                    result.append(summ // 5)
                    result.append(y + 1)
                    result.append(x + 1)

            elif board[y][x-1] != check[0] and board[y][x+1] != check[0]:
                if summ == 5 or summ == 10:
                    result.append(summ//5)
                    result.append(y+1)
                    result.append(x+1)


for x in range(len(board[0])):
    for y in range(len(board)-4):
        summ = 0
        check = set()

        for i in range(5):
            summ += board[y+i][x]
            check.add(board[y+i][x])
        check = list(check)

        if len(check) == 1:
            if y == 0 and board[y+5][x] != check[0]:
                if summ == 5 or summ == 10:
                    result.append(summ // 5)
                    result.append(y + 1)
                    result.append(x + 1)

            elif board[y-1][x] != check[0] and board[y+1][x] != check[0]:
                if summ == 5 or summ == 10:
                    result.append(summ//5)
                    result.append(y+1)
                    result.append(x+1)

for y in range(len(board)-4):
    for x in range(len(board[y])-4):
        summ = 0
        check = set()

        for i in range(5):
            summ += board[y+i][x+i]
            check.add(board[y+i][x+i])
        check = list(check)

        if len(check) == 1:
            if x == 0 or y == 0:
                if x == len(board[y])-5 or y == len(board)-5:
                    continue
                if board[y+5][x+5] != check[0]:
                    if summ == 5 or summ == 10:
                        result.append(summ // 5)
                        result.append(y + 1)
                        result.append(x + 1)

            elif board[y-1][x-1] != check[0] and board[y+5][x+5] != check[0]:
                if summ == 5 or summ == 10:
                    result.append(summ//5)
                    result.append(y+1)
                    result.append(x+1)

for y in range(len(board)-4):
    for x in range(len(board[y])-1,3,-1):
        summ = 0
        check = set()
        for i in range(5):
            summ += board[y+i][x-i]
            check.add(board[y+i][x-i])
        check = list(check)

        if len(check) == 1:
            if x == len(board[y])-1 or y == 0:
                if x == 0 or y == 0:
                    if x == len(board[y])-5 or y == len(board)-5:
                        continue

            elif board[y-1][x+1] != check[0] and board[y+5][x-5] != check[0]:
                if summ == 5 or summ == 10:
                    result.append(summ//5)
                    result.append(y+1)
                    result.append(x+1)

if len(result) == 0:
    print(0)
if result[0] == 1:
    print(1)
    print(result[1],result[2])
if result[0] == 2:
    print(2)
    print(result[1],result[2])
