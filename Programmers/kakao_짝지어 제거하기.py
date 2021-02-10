def solution(s):
    stack = []
    for i in range(len(s)):
        if stack:
            if stack[-1] == s[i]:
                stack.pop()
                continue
        stack.append(s[i])
    if not stack:
        return 1
    return 0

print(solution('abccaeeaba'))
print(solution('cdcd'))