def solution(number, k):
    answer = ''
    N = len(number) - k
    stack = [int(number[0])]
    for i in range(1, len(number)):
        num = int(number[i])
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    stack = stack[:N]
    for i in range(len(stack)):
        answer += str(stack[i])
    return answer

print(solution('1924', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))