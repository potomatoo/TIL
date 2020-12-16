def solution(d, budget):
    d.sort()
    answer = 0
    check = 0
    for i in range(len(d)):
        check += d[i]
        answer += 1
        if check > budget:
            answer -= 1
            break
        if check == budget:
            break
    return answer

print(solution([2,2,3,3], 10))