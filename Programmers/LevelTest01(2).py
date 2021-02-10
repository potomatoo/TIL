def solution(d, budget):
    answer = 0
    d.sort()
    check = 0
    for i in range(len(d)):
        if check + d[i] > budget:
            break
        check += d[i]
        answer += 1

    return answer

print(solution([1,3,2,5,4], 9))