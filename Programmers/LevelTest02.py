def solution(s):
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

print(solution('()()'))
print(solution('(())()'))
print(solution(')()('))
print(solution('(()('))