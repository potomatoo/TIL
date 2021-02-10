import math
def solution(n, k):
    answer = [num for num in range(1,n+1)]
    answer_list = []
    while n > 0 :
        n -= 1
        share, remainder = divmod(k,math.factorial(n))
        if not remainder: share -= 1
        answer_list.append(answer[share])
        answer.remove(answer[share])
        k = remainder
    return answer_list

print(solution(20, 5))