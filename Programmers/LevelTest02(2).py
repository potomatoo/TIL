def solution(n, t, m, p):
    answer = ''
    def trans_n(num, k):
        order = '0123456789ABCDEF'
        if num < k:
            return order[num]
        trans = ''
        while num // k >= 1:
            remain = order[num % k]
            num = num // k
            trans = remain + trans
            if num < k:
                trans = order[num] + trans
        return trans
    mid_answer = ''
    for i in range(m*t):
        mid_answer += trans_n(i, n)

    for i in range(p-1, m*t, m):
        answer += mid_answer[i]

    return answer



print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))


