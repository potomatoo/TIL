def solution(numbers):
    answer = ""
    s_numbers = []
    if not sum(numbers):
        return "0"
    for i in range(len(numbers)):
        s_numbers.append(str(numbers[i]) * 3)
    s_numbers.sort(reverse=True)
    for i in range(len(s_numbers)):
        n = len(s_numbers[i]) // 3
        answer += s_numbers[i][:n]

    return answer

print(solution([0,0,0,0,0,0]))