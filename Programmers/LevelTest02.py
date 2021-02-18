def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        time = 0
        flag = True
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                time += 1
                answer.append(time)
                flag = False
                break
            time += 1
        if flag:
            answer.append(time)
    return answer + [0]

print(solution([1, 2, 3, 2, 3]))