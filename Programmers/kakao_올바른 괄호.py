def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            close = stack.pop()
            if close == s[i]:
                return False
    if stack:
        return False
    else:
        return True

print(solution(")()("))