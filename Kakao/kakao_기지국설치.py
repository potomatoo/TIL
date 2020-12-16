import itertools
from copy import deepcopy

n = 16
stations = [9]
w = 2

def solution(n, stations, w):
    board = [1 for _ in range(n)]
    check = [x for x in range(n)]

    for station in stations:
        station = station-1
        board[station] = 0

        for i in range(1, w+1):
            if station - i >= 0:
                board[station-i] = 0

            if station + i <= n-1:
                board[station+i] = 0

    board2 = []
    for i in range(n):
        if board[i]:
            board2.append(check[i])

    answer = 0
    check_stop = False

    for i in range(1, n):
        coms = list(itertools.combinations(board2, i))
        for com in coms:
            c_board = deepcopy(board)
            for c in com:
                c_board[c] = 0
                for j in range(1, w + 1):
                    if c - j >= 0:
                        c_board[c - j] = 0
                    if c + j <= n - 1:
                        c_board[c + j] = 0

            is_full = True
            for k in range(n):
                if c_board[k]:
                    is_full = False
                    break

            if is_full:
                check_stop = True
                break

        if check_stop:
            answer = i
            break

    return answer

print(solution(n, stations, w))