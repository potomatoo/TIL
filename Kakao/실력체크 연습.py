'''
def solution(n, t, m, p):
    def change(num, k):
        d = "0123456789ABCDEF"
        q, r = divmod(num, k)
        if q == 0:
            return d[r]
        else:
            return change(q, k) + d[r]

    check = []
    for i in range(t * m):
        mid = change(i, n)
        for j in range(len(mid)):
            check.append(mid[j])

    result = ''
    for i in range(p - 1, len(check), m):
        result += check[i]
        if len(result) == t:
            break
    return result


from itertools import combinations


def solution(people, limit):
    people.sort()
    visit = [0 for _ in range(len(people))]
    cnt = len(people)
    for i in range(len(people)-1):
        if visit[i]:
            continue
        if people[i] + people[i+1] <= limit:
            visit[i], visit[i+1] = 1, 1
            cnt -= 1
    print(visit)
    return cnt

print(solution([20], 100))

def isbalanced(s):
    chk = 0
    for c in s:
        if c == '(':
            chk += 1
        elif c == ')':
            chk -= 1

    if not chk:
        return True
    else:
        return False


def check_correct(s):
    check = []
    for c in s:
        if c == "(":
            check.append(c)
        else:
            if not check:
                return False
            check.pop()
    if not check:
        return True
    else:
        return False


def solution(p):
    if p == '' or check_correct(p):
        return p
    u = v = answer = ''
    for i in range(2, len(p) + 1, 2):
        if isbalanced(p[0:i]):
            u = p[0:i]
            v = p[i:len(p)]
            break

    if check_correct(u):
        answer += u + solution(v)
    else:
        answer += '(' + solution(v) + ')'
        for c in u[1:-1]:
            if c == '(':
                answer += ')'
            else:
                answer += '('

    return answer

print(solution('()))((()'))


import itertools


def solution(expression):
    numbers, operations = [], []
    temp_num = ''
    for i in range(len(expression)):
        if expression[i].isdigit():
            temp_num += expression[i]
        else:
            numbers.append(int(temp_num))
            temp_num = ''
            operations.append(expression[i])
    numbers.append(int(temp_num))

    answer = 0
    for order in itertools.permutations(['+', '-', '*']):
        temp_answer = numbers.copy()
        temp_operations = operations.copy()
        for i in range(len(order)):
            index = 0
            while index < len(temp_operations):
                if temp_operations[index] == order[i]:
                    if temp_operations[index] == '+':
                        temp_answer[index] += temp_answer[index + 1]
                    elif temp_operations[index] == '-':
                        temp_answer[index] -= temp_answer[index + 1]
                    elif temp_operations[index] == '*':
                        temp_answer[index] *= temp_answer[index + 1]
                    temp_operations.pop(index)
                    temp_answer.pop(index + 1)
                else:
                    index += 1
        answer = max(answer, abs(temp_answer[0]))
    return answer

print(solution("100-200*300-500+20"))

def solution(number, k):
    collected = []

    for (i, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1

        if k == 0:
            collected += number[i:]
            break

        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer

print(solution('4177252841', 4))
'''




























