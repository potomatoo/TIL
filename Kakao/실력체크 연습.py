def solution(p):
    def is_correct(q):
        stack = []
        for i in range(len(q)):
            if not stack:
                stack.append(q[i])
                continue
            if stack[-1] == q[i]:
                stack.append(q[i])
            elif stack[-1] == '(' and q[i] == ')':
                stack.pop()
        if stack:
            return False
        else:
            return True

    def get_uv(q):
        stack = [q[0]]
        idx = 0
        for i in range(1, len(q)):
            if not stack:
                break
            if stack[-1] == q[i]:
                stack.append(q[i])
            else:
                idx = i
                stack.pop()
        u = q[:idx + 1]
        v = q[idx + 1:]
        return u, v

    def change_correct(q):
        if not q:
            return ''
        u, v = get_uv(q)

        if is_correct(u):
            return u + change_correct(v)
        else:
            answer = '('
            answer += change_correct(v)
            answer += ')'

            for p in u[1:len(u)-1]:
                if p == '(':
                    answer += ')'
                else:
                    answer += ')'
            return answer
    return change_correct(p)
print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
