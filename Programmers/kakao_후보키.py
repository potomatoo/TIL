from itertools import combinations

def solution(relation):
    answer = []
    idx = [x for x in range(len(relation[0]))]

    for k in range(1, len(relation[0])+1):
        candidate = list(combinations(idx, k))
        print(candidate)
        check_visit = []
        for n in range(len(candidate)):
            check = []
            for row in relation:
                mid_check = ''
                for m in range(len(candidate[n])):
                    mid_check += row[candidate[n][m]]
                check.append(mid_check)

            if check and len(check) == len(set(check)):
                for m in range(len(candidate[n])):
                    flag = True
                    for a in answer:
                        if set(a).issubset(set(candidate[n])):
                            flag = False
                            break
                    if flag:
                        answer.append(candidate[n])
    return len(answer)

print(solution([['b','2','a','a','b'],
['b','2','7','1','b'],
['1','0','a','a','8'],
['7','5','a','a','9'],
['3','0','a','f','9']]))