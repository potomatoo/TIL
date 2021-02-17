def solution(N, stages):
    fail_stage = [0] * (N+2)

    for i in range(1, N+2):
        fail_stage[i] = stages.count(i)
    for i in range(1, N+1):
        arrive_stage = sum(fail_stage[i:])
        if arrive_stage == 0:
            fail_stage[i] = (i, 0)
            continue
        fail_stage[i] = (i, fail_stage[i] / arrive_stage)
    fail_stage = fail_stage[1:-1]
    fail_stage.sort(key=lambda x:[-x[1],x[0]])
    answer = []
    for number, x in fail_stage:
        answer.append(number)

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))