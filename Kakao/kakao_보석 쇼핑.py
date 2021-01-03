# 시간 초과!

def solution(gems):
    answer = [0, 0xfffff]
    check = len(gems)
    kind = len(set(gems))

    for i in range(len(gems)):
        if len(gems) - i > check:
            break
        for j in range(i, i+check):
            if j - i >= check:
                break
            if len(set(gems[i:j+1])) == kind:
                if answer[1] - answer[0] > j+1 - (i+1):
                    answer = [i+1, j+1]
                    check = j+1 - i+1
                    break
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))