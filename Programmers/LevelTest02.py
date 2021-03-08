from itertools import combinations
def solution(relation):
    check = len(relation)
    answer = []
    col = [x for x in range(len(relation[0]))]
    for k in range(1, len(relation[0])+1):
        com = list(combinations(col, k))
        for i in range(len(com)):
            mid_check = set()
            for y in range(check):
                one_check = []
                for j in range(len(com[i])):
                    one_check.append(relation[y][com[i][j]])
                mid_check.add(tuple(one_check))

            if len(mid_check) == check:
                if not answer:
                    answer.append(com[i])
                    continue
                flag = True
                for a in answer:
                    if set(a).issubset(set(com[i])):
                        flag = False
                        break
                if flag:
                    answer.append(com[i])

    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))



