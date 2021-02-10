def solution(n,a,b):
    if a > b:
        a, b = b, a

    def next_round(k):
        if k % 2:
            k //= 2
            k += 1
        else:
            k //= 2
        return k
    answer = 1
    while True:
        if b - a == 1 and a % 2 and not b % 2:
            break
        a = next_round(a)
        b = next_round(b)
        answer += 1

    return answer

print(solution(8, 4 ,7))