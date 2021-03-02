def solution(n, results):
    answer = 0
    win_dic = dict()
    lose_dic = dict()
    for win, lose in results:
        if win not in win_dic:
            win_dic[win] = [lose]
        else:
            win_dic[win].append(lose)
        if lose not in lose_dic:
            lose_dic[lose] = [win]
        else:
            lose_dic[lose].append(win)
    print(win_dic)
    print(lose_dic)
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

