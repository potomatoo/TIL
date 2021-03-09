def solution(s):
    answer = 0xffffff
    def trans_str(s, k):
        new_s = ''
        start_s = mid_s = s[:k]
        s_cnt = 1
        for i in range(k, len(s), k):
            mid_s = s[i:i+k]
            if start_s == mid_s:
                s_cnt += 1
            else:
                if s_cnt == 1:
                    new_s += start_s
                    start_s = mid_s
                else:
                    new_s += (str(s_cnt) + start_s)
                    s_cnt = 1
                    start_s = mid_s
        if s_cnt == 1:
            new_s += mid_s
        else:
            new_s += (str(s_cnt) + start_s)

        return len(new_s)
    for k in range(1, len(s)+1):
        answer = min(answer, trans_str(s, k))

    return answer

print(solution("a"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))



