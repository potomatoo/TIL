def rotate(now_s):
    changed_s = ''
    for i in range(1, len(now_s)):
        changed_s += now_s[i]
    changed_s += now_s[0]
    return changed_s

def check(now_s):
    if now_s[0] == ')' or now_s[0] == '}' or now_s[0] == ']':
        return False
    stack = [now_s[0]]
    for i in range(1, len(now_s)):
        if now_s[i] == '(' or now_s[i] == '{' or now_s[i] == '[':
            stack.append(now_s[i])
        else:
            flag = False
            if now_s[i] == ')':
                while stack:
                    popped = stack.pop()
                    if popped == '(':
                        flag = True
                        break
            elif now_s[i] == '}':
                while stack:
                    popped = stack.pop()
                    if popped == '{':
                        flag = True
                        break
            elif now_s[i] == ']':
                while stack:
                    popped = stack.pop()
                    if popped == '[':
                        flag = True
                        break
            if not flag:
                return False

    if stack:
        return False
    return True

def solution(s):
    answer = 0
    for _ in range(len(s)):
        now_s = rotate(s)
        if check(now_s):
            answer += 1
        s = now_s
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))