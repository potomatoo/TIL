from itertools import combinations

def solution(orders, course):
    order = []
    for i in range(len(orders)):
        order_list = (','.join(orders[i])).split(',')
        order.append(set(order_list))

    results = []
    for k in course:
        answer_len = 0
        answer_set = set()
        for i in range(len(orders)):
            if len(orders[i]) >= k:
                com = list(combinations(orders[i], k))
                for c in com:
                    mid_answer = 0
                    compare = set(c)
                    for j in range(len(orders)):
                        if compare.issubset(order[j]):
                            mid_answer += 1
                    if mid_answer > answer_len and mid_answer > 1:
                        answer_len = mid_answer
                        mid_word = ''
                        compare_list = list(compare)
                        for cw in range(len(compare_list)):
                            mid_word += compare_list[cw]
                        answer_set = set()
                        answer_set.add(mid_word)

                    if mid_answer == answer_len and mid_answer > 1:
                        mid_word = ''
                        compare_list = list(compare)
                        compare_list.sort()
                        for cw in range(len(compare_list)):
                            mid_word += compare_list[cw]
                        answer_set.add(mid_word)
        if answer_len:
            results.append(answer_set)
    print(results)
    answer = []
    for result in results:
        for one in result:
            two = (','.join(one)).split(',')
            two.sort()
            word = ''
            for i in range(len(two)):
                word += two[i]
            answer.append(word)
    answer = list(set(answer))
    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))