def solution(d, budget):
    answer = 0
    d.sort()
    print(d)
    for cost in d:
        budget -= cost
        answer += 1
        if budget == 0:
            break
        elif budget < 0:
            answer -= 1
            break

    return answer

print(solution([1,3,2,5,4], 9))