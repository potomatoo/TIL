def solution(N, stages):
    mid_answer = [(0, 0)] * (N+1)
    people = len(stages)
    for i in range(1, N+1):
        if people == 0:
            mid_answer[i] = (i, 0)
            continue
        mid_answer[i] = (i, (stages.count(i)/people))
        people -= stages.count(i)
    mid_answer = sorted(mid_answer[1:], key=lambda x:[-x[1], x[0]])
    answer = []
    for idx, fail in mid_answer:
        answer.append(idx)
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
