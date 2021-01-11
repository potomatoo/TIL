# 미해결

from collections import deque

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

def is_rangeout(a, b, c, d, N):
    if a < 0 or b < 0 or c < 0 or d < 0 or a > N - 1 or b > N - 1 or c > N - 1 or d > N - 1:
        return True
    return False

def can_move(cur1, cur2, cost, N, board):
    go_move = []
    for i in range(4):
        ty1, tx1 = dy[i] + cur1[0], dx[i] + cur1[1]
        ty2, tx2 = dy[i] + cur2[0], dx[i] + cur2[1]
        if not is_rangeout(ty1, tx1, ty2, tx2, N):
            if not board[ty1][tx1] and not board[ty2][tx2]:
                go_move.append(((ty1, tx1), (ty2, tx2), cost+1))
    if cur1[0] == cur2[0]:
        if not is_rangeout(cur1[0]-1, cur1[1], cur2[0]-1, cur2[1], N):
            if not board[cur1[0]-1][cur1[1]] and not board[cur2[0]-1][cur2[1]]:
                go_move.append(((cur1[0]-1, cur1[1]), (cur1[0], cur1[1]), cost+1))
                go_move.append(((cur2[0]-1, cur2[1]), (cur2[0], cur2[1]), cost+1))
        if not is_rangeout(cur1[0]+1, cur1[1], cur2[0]+1, cur2[1], N):
            if not board[cur1[0]+1][cur1[1]] and not board[cur2[0]+1][cur2[1]]:
                go_move.append(((cur1[0], cur1[1]), (cur1[0]+1, cur1[1]), cost + 1))
                go_move.append(((cur2[0], cur2[1]), (cur2[0]+1, cur2[1]), cost + 1))
    else:
        if not is_rangeout(cur1[0], cur1[1]-1, cur2[0], cur2[1]-1, N):
            if not board[cur1[0]][cur1[1]-1] and not board[cur2[0]][cur2[1]-1]:
                go_move.append(((cur1[0], cur1[1]-1), (cur1[0], cur1[1]), cost+1))
                go_move.append(((cur2[0], cur2[1]-1), (cur2[0], cur2[1]), cost+1))
        if not is_rangeout(cur1[0], cur1[1]+1, cur2[0], cur2[1]+1, N):
            if not board[cur1[0]][cur1[1]+1] and not board[cur2[0]][cur2[1]+1]:
                go_move.append(((cur1[0], cur1[1]), (cur1[0], cur1[1]+1), cost+1))
                go_move.append(((cur2[0], cur2[1]), (cur2[0], cur2[1]+1), cost+1))

    return go_move

def solution(board):
    N = len(board)
    Q = deque()
    Q.append(((0, 0), (0, 1), 0))
    visit = [((0, 0), (0, 1))]
    while Q:
        cur1, cur2, cost = Q.popleft()
        if cur1 == (N-1, N-1) or cur2 == (N-1, N-1):
            return cost
        for new1, new2, new_cost in can_move(cur1, cur2, cost, N, board):
            if (new1, new2) not in visit:
                visit.append((new1, new2))
                Q.append((new1, new2, new_cost))


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))