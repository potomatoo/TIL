# 실패!

from itertools import permutations

def solution(board, r, c):
    card = []
    card_set = set()
    for y in range(4):
        for x in range(4):
            if board[y][x]:
                card.append((board[y][x], y, x, 0))
                card_set.add(board[y][x])

    def find_same_card(n, y, x, click):
        for i in range(len(card)):
            if card[i][0] == n and card[i][3] == 0:
                if card[i][1] == y or card[i][2] == x:
                    same_card = (card[i][1], card[i][2], click + 2)
                    card[i] = (card[i][0], card[i][1], card[i][2], 1)
                    return same_card
                else:
                    same_card = (card[i][1], card[i][2], click + 3)
                    card[i] = (card[i][0], card[i][1], card[i][2], 1)
                    return same_card

    def find_start_card(n, y, x, click):
        start_d = 1e9
        start_card = ()
        check_idx = 0
        for i in range(len(card)):
            if card[i][0] == n:
                if abs(card[i][1]-y) + abs(card[i][2]-x) < start_d:
                    start_d = abs(card[i][1]-y) + abs(card[i][2]-x)
                    check_idx = i
                    if card[i][1] == y and card[i][2] == x:
                        start_card = (card[i][1], card[i][2], click+1)
                    elif card[i][1] == y or card[i][2] == x:
                        start_card = (card[i][1], card[i][2], click+2)
                    else:
                        start_card = (card[i][1], card[i][2], click + 3)
        card[check_idx] = (card[check_idx][0], card[check_idx][1], card[check_idx][2], 1)
        return start_card

    per = permutations(list(card_set), len(card_set))
    answer = 1e9
    for order in per:
        y, x, click = r, c, 0
        for num in order:
            y, x, click = find_start_card(num, y, x, click)
            y, x, click = find_same_card(num, y, x, click)
        for i in range(len(card)):
            card[i] = (card[i][0], card[i][1], card[i][2], 0)
        answer = min(answer, click)

    return answer