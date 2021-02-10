def solution(n):
    def numnary(num, k):
        result = ''
        if num == 1:
            return '1'
        while num // k >= 1:
            remain = num % k
            num = num // k
            result = str(remain) + result
            if num < k:
                result = str(num) + result
        return result
    new_num = numnary(n, 3)
    answer = 0
    for i in range(len(new_num)):
        answer += (3**(i)) * int(new_num[i])
    return answer

print(solution(1))

