def solution(n, s):
    answer = []
    k = s // n
    remain = s % n
    if k == 0:
        return [-1]
    for i in range(n):
        answer.append(k)

    cnt = 0
    while remain:
        answer[cnt] = k+1
        cnt += 1
        remain -= 1
    answer.sort()
    return answer

print(solution(2, 9))