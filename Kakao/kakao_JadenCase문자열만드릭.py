def solution(s):
    answer = ""
    jump = []
    before = s[0]
    one_jump = 0

    for i in range(len(s)):
        if i == len(s) - 1 and s[i] == " " and before == " ":
            jump.append(one_jump + 1)
        if i == len(s) - 1 and s[i] == " " and before != " ":
            jump.append(1)
        if s[i] == " " and before != " ":
            one_jump = 1
        elif s[i] == " " and before == " ":
            one_jump += 1
        elif s[i] != " " and before == " ":
            jump.append(one_jump)

        before = s[i]

    string = s.split()

    if s[0] != " ":
        for i in range(len(string)):
            if i == len(string) -1:
                answer += string[i].capitalize()
                break
            answer += string[i].capitalize()
            answer += " " * jump[i]

    else:
        for i in range(len(string)):
            answer += " " * jump[i]
            if i == len(string) -1:
                answer += string[i].capitalize()
                break
            answer += string[i].capitalize()

    if s[-1] == " ":
        answer += " " * jump[-1]

    return answer

print(solution("   asdfs Wsdfsdf asdfa  sadassass    d    "))