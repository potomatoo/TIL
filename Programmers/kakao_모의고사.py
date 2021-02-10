def solution(answers):
    person1 = [1,2,3,4,5] * 2000
    person2 = [2,1,2,3,2,4,2,5] * ((10000//8)+1)
    person3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    check = [[1, 0], [2, 0], [3, 0]]
    for i in range(len(answers)):
        if person1[i] == answers[i]:
            check[0][1] += 1
        if person2[i] == answers[i]:
            check[1][1] += 1
        if person3[i] == answers[i]:
            check[2][1] += 1
    check.sort(key=lambda x:-x[1])
    answer = []
    max_cnt = check[0][1]

    for i, cnt in check:
        if cnt != max_cnt:
            break
        answer.append(i)

    return answer

print(solution([1, 2, 3, 4, 5]))