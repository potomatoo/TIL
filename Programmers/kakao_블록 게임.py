def get_block(N, board):
    block = dict()
    for y in range(N):
        for x in range(N):
            if not board[y][x]:
                continue
            if board[y][x] not in block:
                block[board[y][x]] = [(y, x)]
            else:
                block[board[y][x]].append((y, x))
    return block

def is_can_blank(yy, xx, board):
    for z in range(yy+1):
        if board[z][xx]:
            return False
    return True

def get_blank(block, board):
    delete_block = []
    for key in block.keys():
        y_min, x_min = 1e9, 1e9
        same_y = set()
        same_x = set()
        sero_rectangle = [[0 for _ in range(2)] for _ in range(3)]
        garo_rectangle = [[0 for _ in range(3)] for _ in range(2)]
        for y, x in block[key]:
            y_min = min(y_min, y)
            x_min = min(x_min, x)
            same_y.add(y)
            same_x.add(x)
        blank = []
        if len(same_y) == 3:
            for y, x in block[key]:
                sero_rectangle[y-y_min][x-x_min] = 1
            for y in range(3):
                for x in range(2):
                    if not sero_rectangle[y][x]:
                        if is_can_blank(y+y_min, x+x_min, board):
                            blank.append((y+y_min, x+x_min))

        else:
            for y, x in block[key]:
                garo_rectangle[y-y_min][x-x_min] = 1
            for y in range(2):
                for x in range(3):
                    if not garo_rectangle[y][x]:
                        if is_can_blank(y+y_min, x+x_min, board):
                            blank.append((y+y_min, x+x_min))

        if len(blank) == 2:
            delete_block.append(key)

    if not delete_block:
        return board, 0
    else:
        for k in delete_block:
            for y, x in block[k]:
                board[y][x] = 0

        return board, len(delete_block)


def solution(board):
    answer = 0
    N = len(board)

    while True:
        block = get_block(N, board)
        mid_board, mid_answer = get_blank(block, board)
        if not mid_answer:
            break
        answer += mid_answer
        board = mid_board

    return answer

print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))