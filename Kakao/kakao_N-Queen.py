cnt = 0
def solution(n):
    global cnt
    col = [0] * n
    up_cross = [0] * ((2*n)-1)
    down_cross = [0] * ((2 * n) - 1)
    def n_queen(c):
        global cnt
        if c == n:
            cnt += 1
            return
        for r in range(n):
            if not col[r] and not up_cross[r+c] and not down_cross[n+r-c-1]:
                col[r] = 1
                up_cross[r+c] = 1
                down_cross[n+r-c-1] = 1
                n_queen(c+1)
                col[r] = 0
                up_cross[r + c] = 0
                down_cross[n + r - c - 1] = 0

    n_queen(0)
    return cnt

print(solution(4))