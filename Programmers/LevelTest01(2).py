def solution(s):
    answer = ''
    s = s.split()
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j % 2:
                answer += s[i][j].lower()
            else:
                answer += s[i][j].upper()
        if i != len(s)-1:
            answer += ' '

    return answer

print(solution('try hello world'))
print(solution('ts yee sdddd'))
