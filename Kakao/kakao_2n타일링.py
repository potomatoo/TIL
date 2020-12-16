n = 7

def solution(n):
    a = 1
    b = 2

    for i in range(n-1):
        c = a + b
        a = b
        b = c
    answer = a
    return answer



print(solution(n))