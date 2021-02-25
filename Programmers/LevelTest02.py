def solution(number, k):
    answer = ''
    stack = [int(number[0])]
    for i in range(1, len(number)):
        while stack and stack[-1] < int(number[i]) and k > 0:
            stack.pop()
            k -= 1
        stack.append(int(number[i]))
    stack = stack[:(len(number)-k)]
    for n in stack:
        answer += str(n)
    return answer

print(solution('1924', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))
