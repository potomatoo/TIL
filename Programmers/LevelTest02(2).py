def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        cnt = 1
        flag = True
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(cnt)
                flag = False
                break
            cnt += 1
        if flag:
            answer.append(cnt-1)
    return answer + [0]

print(solution([1, 2, 3, 2, 3]))



