def is_right(s):
    if s[0] == ')':
        return False
    stack = []
    for i in range(len(s)):
        if s[i] == ')' and stack:
            stack.pop()
        else:
            stack.append(s[i])
    if stack:
        return False
    return True

def make_right(s):
    if not s:
        return s
    left_cnt = 0
    right_cnt = 0
    u = ''
    for i in range(len(s)):
        if s[i] == '(':
            left_cnt += 1
            u += s[i]
        else:
            right_cnt += 1
            u += s[i]
        if left_cnt == right_cnt:
            break
    v = s[left_cnt*2:]
    if is_right(u):
        v = make_right(v)
        return u + v
    else:
        v = make_right(v)
        v = '(' + v
        v += ')'
        new_u = u[1:-1]
        u = ''
        for i in range(len(new_u)):
            if new_u[i] == '(':
                u += ')'
            else:
                u += '('
        return v + u

def solution(p):
    if is_right(p):
        return p
    return make_right(p)


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))