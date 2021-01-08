# 시간초과!

from copy import deepcopy

cnt = 1
def solution(n, k):
    answer = []
    def combination(idx):
        global cnt
        if idx == n:
            if cnt == k:
                answer.append(deepcopy(order))
                return
            cnt += 1
            return
        for i in range(n):
            if visit[i]:
                continue
            order.append(board[i])
            visit[i] = 1
            combination(idx+1)
            visit[i] = 0
            order.pop()
    order = []
    board = [x for x in range(1, n+1)]
    visit = [0 for _ in range(n+1)]
    combination(0)
    return answer[0]


print(solution(20, 5))