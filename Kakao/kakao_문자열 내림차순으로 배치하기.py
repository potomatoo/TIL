def solution(s):
    answer = ''
    sort_ls = sorted(s, reverse=True)
    for i in range(len(sort_ls)):
        answer += sort_ls[i]
    return answer

print(solution('Zbcdefg'))