def solution(s):
    answer = ''
    idx = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            idx = 0
            continue
        if idx == 0:
            answer += s[i].upper()
            idx += 1
        elif idx % 2:
            answer += s[i].lower()
            idx += 1
        else:
            answer += s[i].upper()
            idx += 1

    return answer

print(solution('try hello world	'))