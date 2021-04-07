from itertools import permutations

def solution(board, r, c):
    card = []
    card_set = set()
    for y in range(4):
        for x in range(4):
            if board[y][x]:
                card.append((board[y][x], y, x))
                card_set.add(board[y][x])

    def find_card(ny, nx, y, x, click):
        if ny == y and nx == x:
            start_card = (ny, nx, click+1)
        elif ny == y or nx == x:
            start_card = (ny, nx, click+2)
        else:
            start_card = (ny, nx, click + 3)
        return start_card

    per = permutations(card, len(card))
    answer = 1e9
    for order in per:
        flag = True
        for i in range(0, len(order), 2):
            if order[i][0] != order[i+1][0]:
                flag = False
                break
        if not flag:
            continue
        y, x, click = r, c, 0
        for num in order:
            y, x, click = find_card(num[1], num[2], y, x, click)
        answer = min(answer, click)

    return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))