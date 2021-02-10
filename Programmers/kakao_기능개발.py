import math

def solution(progresses, speeds):
    check = []
    for i in range(len(progresses)):
        day = (100 - progresses[i]) / speeds[i]
        remain = (100 - progresses[i]) % speeds[i]
        if remain:
            check.append(math.trunc(day+1))
        else:
            check.append(math.trunc(day))

    before = check[0]
    time = 1
    answer= []
    for num in check[1:]:
        if num <= before:
            time += 1
        else:
            answer.append(time)
            before = num
            time = 1

    answer.append(time)
    return answer

