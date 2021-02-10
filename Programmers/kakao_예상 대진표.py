def solution(n,a,b):
    answer = 1
    while True:
        if abs(a-b) == 1 and (a//2 != b//2):
            break
        if a % 2:
            a = (a//2)+1
        else:
            a = a // 2
        if b % 2:
            b = (b//2)+1
        else:
            b = b//2
        answer += 1

    return answer

print(solution(8, 4, 7))