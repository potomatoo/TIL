def solution(n):
    answer = ''
    new_n = str(n)
    new_n = ','.join(new_n)
    new_n = new_n.split(',')
    new_n.sort(reverse=True)
    for i in range(len(new_n)):
        answer += new_n[i]
    return int(answer)

print(solution(118372))
