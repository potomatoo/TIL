def solution(n):
    answer = 0
    now = 1
    while True:
        if now == n:
            break
        check = 0
        for i in range(now, n):
            check += i
            if check >= n:
                break
        if check == n:
            answer += 1
        now += 1

    return answer+1

print(solution(15))