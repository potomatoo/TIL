answer = 0
def solution(n):
    global answer
    v_col = [0] * n
    up_cross = [0] * ((2*n)-1)
    down_cross = [0] * ((2*n)-1)
    def n_queen(row):
        global answer
        if row == n:
            answer += 1
        for col in range(n):
            if not v_col[col] and not up_cross[col+row] and not down_cross[n+row-col-1]:
                v_col[col] = 1
                up_cross[col+row] = 1
                down_cross[n+row-col-1] = 1
                n_queen(row+1)
                v_col[col] = 0
                up_cross[col + row] = 0
                down_cross[n + row-col - 1] = 0
    n_queen(0)
    return answer


print(solution(4))
