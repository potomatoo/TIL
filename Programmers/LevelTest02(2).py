def transN(n):
    if n == 1:
        return 1
    answer = ''
    while n // 2 >= 1:
        remain = n % 2
        n = n // 2
        answer = str(remain) + answer
        if n < 2:
            answer = str(n) + answer
    return answer.count('1')

def solution(n):
    check = transN(n)
    while True:
        n += 1
        if transN(n) == check:
            return n


print(solution(78))
print(solution(15))

