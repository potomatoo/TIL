def solution(n, t, m, p):
    def transN(number, n):
        number_arr = '0123456789ABCDEF'
        answer = ''
        if number < n:
            return number_arr[number]
        while number // n >= 1:
            remain = number % n
            number = number // n
            answer = str(number_arr[remain]) + answer

            if n > number:
                answer = str(number_arr[number]) + answer

        return answer
    answer = ''
    for i in range(t * m):
        answer += transN(i, n)

    result = ''
    for s in range(p-1, t*m, m):
        result += answer[s]
    return result

print(solution(16, 16, 2, 1))