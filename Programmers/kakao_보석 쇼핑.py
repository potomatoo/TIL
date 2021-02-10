# 실패!

def solution(gems):
    answer = []
    kind = len(set(gems))
    check_ls = []
    check = set()
    end = 0
    for start in range(len(gems)):
        while len(check_ls) < len(gems) and end < len(gems):
            for gem in check_ls:
                check.add(gem)
                if len(check) == kind:
                    print(check_ls)
                    answer.append((start + 1, end))
            check_ls.append(gems[end])
            end += 1
        check = set()
        check_ls.remove(gems[start])



    answer.sort(key=lambda x:[abs(x[1]-x[0]), x[0]])
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))